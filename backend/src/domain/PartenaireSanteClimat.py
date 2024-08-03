from src.DatabaseConfig import db
from typing import List


class PartenaireSanteClimat(db.Model):
    __tablename__ = "PartenaireSanteClimat"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_du_partenaire = db.Column(db.Integer, nullable=False)  # Primary key ?
    nom_du_partenaire = db.Column(db.String(255), nullable=False)
    texte_descriptif = db.Column(db.TEXT, nullable=False)
    lien_logo = db.Column(db.String(255), nullable=False)
    titre_actualites = db.Column(db.TEXT, nullable=False)
    texte_actualites = db.Column(db.TEXT, nullable=False)

    # TODO: Adding relationships

    @classmethod
    def find_by_id(cls, _id) -> "PartenaireSanteClimat":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["PartenaireSanteClimat"]:
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
