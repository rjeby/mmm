from src.DatabaseConfig import db
from typing import List


class MembreFamille(db.Model):
    __tablename__ = "MembreFamille"
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

    # TODO: Adding relationships
    inscrit_id = db.Column(
        db.Integer,
        db.ForeignKey("Inscrit.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )
    inscrit = db.relationship(
        "Inscrit", lazy="subquery", primaryjoin="MembreFamille.inscrit_id == Inscrit.id"
    )

    @classmethod
    def find_by_id(cls, _id) -> "MembreFamille":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["MembreFamille"]:
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
