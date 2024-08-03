from typing import List
from src.domain.Menu import Menu
from src.domain.PetitDejeuner import PetitDejeuner
from src.domain.Encas import Encas
from src.DatabaseConfig import db
from datetime import date

InscritProgrammeHebdomadaire = db.Table(
    "InscritProgrammeHebdomadaire",
    db.Column(
        "inscrit_id",
        db.Integer,
        db.ForeignKey("Inscrit.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    ),
     db.Column(
        "programme_hebdomadaire_id",
        db.Integer,
        db.ForeignKey("ProgrammeHebdomadaire.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True,
    )
)


class ProgrammeHebdomadaire(db.Model):
    __tablename__ = "ProgrammeHebdomadaire"
    # Primary key: (inscrit_id, date)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    default = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today) # TODO: Change default value when proposing menus automatically
    vinaigrette_semaine_id = db.Column(db.Integer, db.ForeignKey("Vinaigrette.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    petit_dejeuner_0_id = db.Column(db.Integer, db.ForeignKey("PetitDejeuner.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    petit_dejeuner_0_count = db.Column(db.Integer, nullable=False, default=4)
    petit_dejeuner_1_id = db.Column(db.Integer, db.ForeignKey("PetitDejeuner.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    petit_dejeuner_1_count = db.Column(db.Integer, nullable=False, default=3)
    lundi_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    lundi_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    lundi_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    mardi_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    mardi_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    mardi_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    mercredi_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    mercredi_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    mercredi_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    jeudi_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    jeudi_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    jeudi_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    vendredi_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    vendredi_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    vendredi_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    samedi_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    samedi_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    samedi_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    dimanche_encas_id = db.Column(db.Integer, db.ForeignKey("Encas.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    dimanche_dejeuner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    dimanche_diner_id = db.Column(db.Integer, db.ForeignKey("Menu.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    # TODO: Adding relationships
    petit_dejeuner_0 = db.relationship("PetitDejeuner", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.petit_dejeuner_0_id == PetitDejeuner.id")
    petit_dejeuner_1 = db.relationship("PetitDejeuner", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.petit_dejeuner_1_id == PetitDejeuner.id")
    lundi_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.lundi_encas_id == Encas.id")
    lundi_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.lundi_dejeuner_id == Menu.id")
    lundi_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.lundi_diner_id == Menu.id")
    mardi_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.mardi_encas_id == Encas.id")
    mardi_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.mardi_dejeuner_id == Menu.id")
    mardi_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.mardi_diner_id == Menu.id")
    mercredi_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.mercredi_encas_id == Encas.id")
    mercredi_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.mercredi_dejeuner_id == Menu.id")
    mercredi_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.mercredi_diner_id == Menu.id")
    jeudi_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.jeudi_encas_id == Encas.id")
    jeudi_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.jeudi_dejeuner_id == Menu.id")
    jeudi_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.jeudi_diner_id == Menu.id")
    venedredi_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.vendredi_encas_id == Encas.id")
    vendredi_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.vendredi_dejeuner_id == Menu.id")
    vendredi_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.vendredi_diner_id == Menu.id")
    samedi_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.samedi_encas_id == Encas.id")
    samedi_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.samedi_dejeuner_id == Menu.id")
    samedi_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.samedi_diner_id == Menu.id")
    dimanche_encas = db.relationship("Encas", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.dimanche_encas_id == Encas.id")
    dimanche_dejeuner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.dimanche_dejeuner_id == Menu.id")
    dimanche_diner = db.relationship("Menu", lazy="subquery", primaryjoin="ProgrammeHebdomadaire.dimanche_diner_id == Menu.id")

    @classmethod
    def find_by_id(cls, _id) -> "ProgrammeHebdomadaire":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls, page, per_page) -> List["ProgrammeHebdomadaire"]:
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