from src.DatabaseConfig import db
from src.domain.Ciqual import Ciqual
from typing import List


IngredientsExclus = db.Table(
    "Ingredients Exclus",
    db.Column(
        "preferences_id",
        db.Integer,
        db.ForeignKey("Preferences.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
    db.Column(
        "ingredient_id",
        db.Integer,
        db.ForeignKey("Ciqual.alim_code", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
)


class Preferences(db.Model):
    __tablename__ = "Preferences"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_alimentation = db.Column(
        db.String(255), nullable=False, default="Méditerranéene"
    )
    difficulte_menu = db.Column(db.String(255), nullable=False, default="Facile")
    nbr_repas_viande_semaine = db.Column(db.Integer, nullable=False, default=3)
    nbr_repas_poisson_semaine = db.Column(db.Integer, nullable=False, default=2)
    preference_viande = db.Column(db.String(255), nullable=False, default="Midi")
    petit_dejeuner = db.Column(db.String(255), nullable=False, default="Sucré")
    jour_courses = db.Column(db.String(255), nullable=False, default="Samedi")
    jour_debut_semaine = db.Column(db.String(255), nullable=False, default="Lundi")
    jour_semaine_suivante = db.Column(db.String(255), nullable=False, default="Jeudi")
    lundi_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    lundi_diner_max = db.Column(db.String(255), nullable=False, default="20 min")
    mardi_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    mardi_diner_max = db.Column(db.String(255), nullable=False, default="30 min")
    mercredi_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    mercredi_diner_max = db.Column(db.String(255), nullable=False, default="30 min")
    jeudi_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    jeudi_diner_max = db.Column(db.String(255), nullable=False, default="20 min")
    vendredi_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    vendredi_diner_max = db.Column(db.String(255), nullable=False, default="30 min")
    samedi_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    samedi_diner_max = db.Column(db.String(255), nullable=False, default="60 min")
    dimanche_dejeuner_max = db.Column(db.String(255), nullable=False, default="20 min")
    dimanche_diner_max = db.Column(db.String(255), nullable=False, default="60 min")
    ingredients_exclus = db.relationship(
        "Ciqual", secondary=IngredientsExclus, lazy="subquery"
    )

    # TODO: Adding relationships

    inscrit_id = db.Column(
        db.Integer,
        db.ForeignKey("Inscrit.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        unique=True,
    )

    @classmethod
    def find_by_id(cls, _id) -> "Preferences":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_inscrit_id(cls, _id) -> "Preferences":
        return cls.query.filter_by(inscrit_id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Preferences"]:
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
