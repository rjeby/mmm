from typing import List
from src.domain.MembreFamille import MembreFamille
from src.domain.Preferences import Preferences
from src.domain.Ciqual import Ciqual
from src.domain.ProgrammeHebdomadaire import ProgrammeHebdomadaire, InscritProgrammeHebdomadaire
from src.DatabaseConfig import db

class Inscrit(db.Model):
    __tablename__ = "Inscrit"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prenom = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    annee_naissance = db.Column(db.Integer, nullable=False)
    taille = db.Column(db.Integer, nullable=False)
    poids = db.Column(db.Integer, nullable=False)
    activite_legere = db.Column(db.String(255), nullable=False)
    activite_moyenne = db.Column(db.String(255), nullable=False)
    activite_elevee = db.Column(db.String(255), nullable=False)
    perdre_poids = db.Column(db.String(255), nullable=False)
    code_postal = db.Column(db.String(255), nullable=False)

    # TODO: Adding relationships
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
        unique=True,
    )
    user = db.relationship(
        "User", lazy="subquery", primaryjoin="Inscrit.user_id == User.id"
    )
    preferences = db.relationship(
        "Preferences",
        lazy="subquery",
        primaryjoin="Inscrit.id == Preferences.inscrit_id",
        uselist=False,
    )
    membres_famille = db.relationship("MembreFamille", lazy="subquery", viewonly=True)
    programme_hebdomadaire = db.relationship(
        "ProgrammeHebdomadaire", secondary="InscritProgrammeHebdomadaire", lazy="subquery"
    )

    @classmethod
    def find_by_id(cls, _id) -> "Inscrit":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_user_id(cls, _id) -> "Inscrit":
        return cls.query.filter_by(user_id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Inscrit"]:
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
