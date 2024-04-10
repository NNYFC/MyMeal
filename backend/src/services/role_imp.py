from sqlalchemy.orm import Session

from backend.src.dto.role_dto import RoleDto
from backend.src.model.role import Role


def get_role_by_name(db: Session, name: str):
    return db.query(Role).filter(Role.name == name).first()


def create_role(db: Session, role: RoleDto):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role
