import uvicorn
from fastapi import FastAPI, Request, HTTPException, Depends
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from starlette.responses import JSONResponse

from backend.src.services import users_imp, role_imp
from backend.src.config.database_config import Settings, DbConnection
from backend.src.dto import user_dto, role_dto
from backend.src.utils.exceptions import UnicornException

settings = Settings()
Base = declarative_base()
db_connect = DbConnection().connect()


# Dependency
def get_db():
    db_session = sessionmaker(bind=db_connect)
    session = db_session()
    try:
        for name in ['ADMIN', 'CLIENT', 'OWNER']:
            role = role_imp.get_role_by_name(db=session, name=name)
            if not role:
                role_imp.create_role(db=session, role=role_dto.RoleDto(name=name))
        yield session
    finally:
        session.close()


def create_tables():
    Base.metadata.create_all(bind=db_connect.connect())


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    return app


application = start_application()


@application.get("/")
async def root():
    return {"message": "Welcome to MyMEAL api!"}


@application.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=exc.status,
        content={"message": f"Server error ! {exc.name} "},
    )


@application.post("/register", response_model=user_dto.UserDto)
async def registration(user: user_dto.User, db: Session = Depends(get_db)):
    try:
        user_exist = users_imp.get_user_by_email(db=db, email=user.email)
        if user_exist:
            raise HTTPException(status_code=400, detail="Email already registered")
        users = users_imp.create_user(db=db, user=user)
    except Exception as e:
        raise UnicornException(name=str(e))
    return users


@application.get("/users", response_model=list[user_dto.UserDto])
async def get_all_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        users = users_imp.get_users(db, skip=skip, limit=limit)
    except Exception as e:
        raise UnicornException(name=str(e))
    return users


if __name__ == '__main__':
    uvicorn.run(app=application, host='127.0.0.1', port=8000)
