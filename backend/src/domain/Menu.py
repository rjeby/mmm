from src.DatabaseConfig import db
from typing import List
from src.domain.Entree import Entree
from src.domain.Plat import Plat
from src.domain.Dessert import Dessert


class Menu(db.Model):
    __tablename__ = "Menu"
    # Primary Key: (entree_id, plat_id, dessert_id)
    id = db.Column(db.Integer, unique=True, nullable=False)
    entree_id = db.Column(db.Integer, 
                          db.ForeignKey("Entree.id", ondelete="CASCADE", onupdate="CASCADE"), 
                          primary_key=True,
                          nullable=False, # TODO: entree_id can be nullable
    )
    plat_id = db.Column(db.Integer, 
                        db.ForeignKey("Plat.id", ondelete="CASCADE", onupdate="CASCADE"), 
                        primary_key=True,
                        nullable=False,
    )
    dessert_id = db.Column(db.Integer, 
                        db.ForeignKey("Dessert.id", ondelete="CASCADE", onupdate="CASCADE"), 
                        primary_key=True,
                        nullable=False, # TODO: dessert_id can be nullable
    )


    # TODO: Adding relationships
    # Entrée / Plat Principal / Dessert
    entree = db.relationship(
        "Entree", lazy="subquery", primaryjoin="Menu.entree_id == Entree.id"
    )
    plat = db.relationship(
        "Plat", lazy="subquery", primaryjoin="Menu.plat_id == Plat.id"
    )
    dessert = db.relationship(
        "Dessert", lazy="subquery", primaryjoin="Menu.dessert_id == Dessert.id"
    )


    @classmethod
    def find_by_id(cls, _id) -> "Menu":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_primary_key(cls, _entree_id, _plat_id, _dessert_id) -> "Menu":
        return cls.query.filter_by(entree_id=_entree_id, plat_id=_plat_id, dessert_id=_dessert_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Menu"]:
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
