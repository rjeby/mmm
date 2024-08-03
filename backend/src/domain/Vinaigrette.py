from typing import List
from src.DatabaseConfig import db


IngredientsVinaigrette = db.Table(
    "IngredientsVinaigrette",
    db.Column(
        "vinaigrette_id",
        db.Integer,
        db.ForeignKey("Vinaigrette.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "ingredient_id",
        db.Integer,
        db.ForeignKey("Ciqual.alim_code", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "ingredient_quantité",
        db.Integer,
        nullable=False
    ),
    db.Column(
        "ingredient_unité",
        db.String( 255),
        nullable=False
    )
)


class Vinaigrette(db.Model):
    __tablename__ = "Vinaigrette"
    id = db.Column(db.Integer, primary_key=True) 
    nom_famille_vinaigrette = db.Column(db.String( 255), nullable=False)
    recette = db.Column(db.String( 512), nullable=False)

    # TODO: Adding relationships
    ingredients = db.relationship(
        "Ciqual", secondary=IngredientsVinaigrette, lazy="subquery"

    )

    @classmethod
    def find_by_id(cls, _id) -> "Vinaigrette":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Vinaigrette"]:
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