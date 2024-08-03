from typing import List
from src.DatabaseConfig import db


IngredientsPlat = db.Table(
    "IngredientsPlat",
    db.Column(
        "plat_id",
        db.Integer,
        db.ForeignKey("Plat.id", ondelete="CASCADE", onupdate="CASCADE"),
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



class Plat(db.Model):
    __tablename__ = "Plat"
    # Primary key should be (num_plat, aliment) but we use id for improving performances
    # TODO: Add unique constraint for the couple (num_plat, aliment)
    id = db.Column(db.Integer, primary_key=True, nullable=False) 
    num_plat = db.Column(db.Integer)
    aliment = db.Column(db.String( 255))
    nom_groupe_plat = db.Column(db.String( 255), nullable=False)
    nom_famille_plat = db.Column(db.String( 255), nullable=False)
    recette = db.Column(db.Text, nullable=False)
    contient_viande = db.Column(db.Boolean, nullable=False)
    contient_poisson = db.Column(db.Boolean, nullable=False)
    indice_glycemique = db.Column(db.String( 255), nullable=False)
    macro_nutriment = db.Column(db.String( 255), nullable=False)
    est_vegetarien = db.Column(db.Boolean, nullable=False)
    contient_gluten = db.Column(db.Boolean, nullable=False)
    est_cetogene = db.Column(db.Boolean, nullable=False)
    duree_preparation = db.Column(db.Integer, nullable=False)
    debut_saison = db.Column(db.String( 255), nullable=False)
    fin_saison = db.Column(db.String( 255), nullable=False)
    prix = db.Column(db.String( 255), nullable=False)
    difficulte = db.Column(db.String( 255), nullable=False)
    est_mediterraneen = db.Column(db.Boolean, nullable=False)
    sans_sel = db.Column(db.String( 255), nullable=False)
    contient_porc = db.Column(db.Boolean, nullable=False)

    # TODO: Adding relationships
    ingredients = db.relationship(
        "Ciqual", secondary=IngredientsPlat, lazy="subquery"
    )

    @classmethod
    def find_by_id(cls, _id) -> "Plat":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Plat"]:
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