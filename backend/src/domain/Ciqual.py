from src.DatabaseConfig import db
from typing import List


class Ciqual(db.Model):
    __tablename__ = "Ciqual"
    alim_grp_code = db.Column(db.Integer, nullable=False)
    alim_ssgrp_code = db.Column(db.Integer, nullable=False)
    alim_ssssgrp_code = db.Column(db.Integer, nullable=False)
    rayon = db.Column(db.String(255), nullable=False)
    alim_code = db.Column(db.Integer, primary_key=True, nullable=False)
    alim_nom_fr = db.Column(db.String(255), nullable=False)
    energieKj = db.Column(db.Float, nullable=False)
    energieKcal = db.Column(db.Float, nullable=False)
    fibres = db.Column(db.Float, nullable=False)
    calcium = db.Column(db.Float, nullable=False)
    cuivre = db.Column(db.Float, nullable=False)
    fer = db.Column(db.Float, nullable=False)
    iode = db.Column(db.Float, nullable=False)
    magnesium = db.Column(db.Float, nullable=False)
    manganese = db.Column(db.Float, nullable=False)
    phosphore = db.Column(db.Float, nullable=False)
    potassium = db.Column(db.Float, nullable=False)
    selenium = db.Column(db.Float, nullable=False)
    sodium = db.Column(db.Float, nullable=False)
    zinc = db.Column(db.Float, nullable=False)
    vitamineA = db.Column(db.Float, nullable=False)
    vitamineD = db.Column(db.Float, nullable=False)
    vitamineE = db.Column(db.Float, nullable=False)
    vitamineK1 = db.Column(db.Float, nullable=False)
    vitamineC = db.Column(db.Float, nullable=False)
    vitamineB1 = db.Column(db.Float, nullable=False)
    vitamineB2 = db.Column(db.Float, nullable=False)
    vitamineB3 = db.Column(db.Float, nullable=False)
    vitamineB5 = db.Column(db.Float, nullable=False)
    vitamineB6 = db.Column(db.Float, nullable=False)
    vitamineB9 = db.Column(db.Float, nullable=False)
    vitamineB12 = db.Column(db.Float, nullable=False)

    # TODO: Adding relationships

    @classmethod
    def find_by_id(cls, _alim_code) -> "Ciqual":
        return cls.query.filter_by(alim_code=_alim_code).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["Ciqual"]:
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
