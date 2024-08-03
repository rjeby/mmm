from typing import List
from src.domain.Inscrit import Inscrit
from src.DatabaseConfig import db


class Roles:

    ADMIN = "ADMIN"
    USER = "USER"
    PAT = "PAT"
    PartenaireSanteClimat = "PSC"


class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    is_confirmed = db.Column(db.Boolean, nullable=False, default=False)
    has_infos = db.Column(db.Boolean, nullable=False, default=False)

    # TODO: Adding relationships
    inscrit = db.relationship("Inscrit", back_populates="user", uselist=False)
    


    @classmethod
    def find_by_id(cls, _id) -> "User":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_email(cls, email) -> "User":
        user = cls.query.filter_by(email=email).first()
        if user is not None:
            return user
        return None

    @classmethod
    def find_all(cls, page, per_page) -> List["User"]:
        paginate = cls.query.order_by(cls.id).paginate(page=page, per_page=per_page)
        return paginate.items

    @classmethod
    def find_all_count(cls):
        return cls.query.count()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def update_db(self) -> None:
        db.session.merge(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
