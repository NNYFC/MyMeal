import bcrypt
from sqlalchemy.orm import Session

from backend.src.dto import user_dto
from backend.src.model.user import User
from backend.src.services.role_imp import get_role_by_name


def get_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    return db_user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_dto.User):
    role = get_role_by_name(db=db, name=user.role_id.name)
    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    fake_hashed_password = bcrypt.hashpw(user.password, salt)
    db_user = User(firstname=user.firstname, lastname=user.lastname,
                   email=user.email, password=fake_hashed_password,
                   phone=user.phone, role_id=role.id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
