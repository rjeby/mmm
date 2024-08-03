from random import randint
from src.domain.ProgrammeHebdomadaire import ProgrammeHebdomadaire, InscritProgrammeHebdomadaire
from src.domain.Menu import Menu
from src.domain.Entree import Entree
from src.domain.Plat import Plat
from src.domain.Dessert import Dessert
from datetime import date
from src.DatabaseConfig import db
from sqlalchemy.sql import func


# Utility function to get a random menu
def get_random_menu(jour):
    # TODO: filter by other preferences
    macroNutrientsDay = planning[jour]
    entree = db.session.query(Entree).filter(Entree.macro_nutriment.in_(macroNutrientsDay)).order_by(func.random()).first()
    plat = db.session.query(Plat).filter(Plat.macro_nutriment.in_(macroNutrientsDay)).order_by(func.random()).first()
    dessert = db.session.query(Dessert).order_by(func.random()).first()
    return Menu.find_by_primary_key(_entree_id=entree.id, _plat_id=plat.id, _dessert_id=dessert.id).id

# Utility function to get a random id from a model
def get_random_id(count):
    return randint(1, count)

# Utility function to create a Porgramme Hebdomadaire entity
def create_programme(default, vinaigrette_count, petit_dejeuner_count, encas_count):
    """
    Creates a ProgrammeHebdomadaire entity with specified parameters.

    Parameters:
    - date (datetime.date): The date associated with the programme.
    - default (bool): Indicates if the programme is a default programme.
    - vinaigrette_count (int): The total number of available vinaigrettes.
    - petit_dejeuner_count (int): The total number of available petit dejeuners.
    - menu_count (int): The total number of available menus.
    - encas_count (int): The total number of available encas.

    Returns:
    - ProgrammeHebdomadaire: An instance of ProgrammeHebdomadaire with randomly assigned IDs for each meal component.
    """
    
    return ProgrammeHebdomadaire(
        date=date.today(),
        default=False,
        vinaigrette_semaine_id=get_random_id(vinaigrette_count),
        petit_dejeuner_0_id=get_random_id(petit_dejeuner_count),
        petit_dejeuner_0_count=4,
        petit_dejeuner_1_id=get_random_id(petit_dejeuner_count),
        petit_dejeuner_1_count=3,
        lundi_encas_id=get_random_id(encas_count),
        lundi_dejeuner_id=get_random_menu("LundiDejeuner"),
        lundi_diner_id=get_random_menu("LundiDiner"),
        mardi_encas_id=get_random_id(encas_count),
        mardi_dejeuner_id=get_random_menu("MardiDejeuner"),
        mardi_diner_id=get_random_menu("MardiDiner"),
        mercredi_encas_id=get_random_id(encas_count),
        mercredi_dejeuner_id=get_random_menu("MercrediDejeuner"),
        mercredi_diner_id=get_random_menu("MercrediDiner"),
        jeudi_encas_id=get_random_id(encas_count),
        jeudi_dejeuner_id=get_random_menu("JeudiDejeuner"),
        jeudi_diner_id=get_random_menu("JeudiDiner"),
        vendredi_encas_id=get_random_id(encas_count),
        vendredi_dejeuner_id=get_random_menu("VendrediDejeuner"),
        vendredi_diner_id=get_random_menu("VendrediDiner"),
        samedi_encas_id=get_random_id(encas_count),
        samedi_dejeuner_id=get_random_menu("SamediDejeuner"),
        samedi_diner_id=get_random_menu("SamediDiner"),
        dimanche_encas_id=get_random_id(encas_count),
        dimanche_dejeuner_id=get_random_menu("DimancheDejeuner"),
        dimanche_diner_id=get_random_menu("DimancheDiner")
)

# Utility function to copy a programme hebdomadaire
def create_default_programme(programme):
    """
    Creates a default ProgrammeHebdomadaire entity based on the provided programme.

    Parameters:
    - programme (ProgrammeHebdomadaire): A ProgrammeHebdomadaire instance with values to use for default fields.

    Returns:
    - ProgrammeHebdomadaire: An instance of ProgrammeHebdomadaire with default values based on the provided programme.
    """
    return ProgrammeHebdomadaire(
        date=date.today(),
        default=True,
        vinaigrette_semaine_id=programme.vinaigrette_semaine_id,
        petit_dejeuner_0_id=programme.petit_dejeuner_0_id,
        petit_dejeuner_0_count=4,
        petit_dejeuner_1_id=programme.petit_dejeuner_1_id,
        petit_dejeuner_1_count=3,
        lundi_encas_id=programme.lundi_encas_id,
        lundi_dejeuner_id=programme.lundi_dejeuner_id,
        lundi_diner_id=programme.lundi_diner_id,
        mardi_encas_id=programme.mardi_encas_id,
        mardi_dejeuner_id=programme.mardi_dejeuner_id,
        mardi_diner_id=programme.mardi_diner_id,
        mercredi_encas_id=programme.mercredi_encas_id,
        mercredi_dejeuner_id=programme.mercredi_dejeuner_id,
        mercredi_diner_id=programme.mercredi_diner_id,
        jeudi_encas_id=programme.jeudi_encas_id,
        jeudi_dejeuner_id=programme.jeudi_dejeuner_id,
        jeudi_diner_id=programme.jeudi_diner_id,
        vendredi_encas_id=programme.vendredi_encas_id,
        vendredi_dejeuner_id=programme.vendredi_dejeuner_id,
        vendredi_diner_id=programme.vendredi_diner_id,
        samedi_encas_id=programme.samedi_encas_id,
        samedi_dejeuner_id=programme.samedi_dejeuner_id,
        samedi_diner_id=programme.samedi_diner_id,
        dimanche_encas_id=programme.dimanche_encas_id,
        dimanche_dejeuner_id=programme.dimanche_dejeuner_id,
        dimanche_diner_id=programme.dimanche_diner_id
    )



# Utility function to retrieve latest programme hebdomadaire
def retrieve_programme_hebdomadaire(id, default):
     programme_hebdomadaire = db.session.query(ProgrammeHebdomadaire).join(
            InscritProgrammeHebdomadaire,
            (InscritProgrammeHebdomadaire.c.programme_hebdomadaire_id == ProgrammeHebdomadaire.id)
        ).filter(
            InscritProgrammeHebdomadaire.c.inscrit_id == id,
            ProgrammeHebdomadaire.default == default
        ).order_by(
            ProgrammeHebdomadaire.id.desc()
        ).first()
     return programme_hebdomadaire

# Planning dictionary
planning = {
    "LundiDejeuner": ["P-L", "L"],
    "LundiDiner": ["P-G", "G"],
    "MardiDejeuner": ["P-G", "G"],
    "MardiDiner": ["P-L", "L"],
    "MercrediDejeuner": ["P-L-G", "L-G"],
    "MercrediDiner": ["P-G", "G"],
    "JeudiDejeuner": ["P-L", "L"],
    "JeudiDiner": ["P-L", "L"],
    "VendrediDejeuner": ["P-L", "L"],
    "VendrediDiner": ["P-G", "G"],
    "SamediDejeuner": ["P-L", "L"],
    "SamediDiner": ["P-L-G", "L-G"],
    "DimancheDejeuner": ["P-L-G", "L-G"],
    "DimancheDiner": ["P-L", "L"]
}

# # Planning map dictionary
# planning_map = {
#     "L-G": "P-L-G",
#     "L": "P-L",
#     "G": "P-G",
#     "P-L-G": "P-L-G",
#     "P-L": "P-L",
#     "P-G": "P-G"
# }
