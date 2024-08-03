import pandas as pd
from src.DatabaseConfig import db
from src.domain.Ciqual import Ciqual
from src.domain.Plat import Plat, IngredientsPlat
from src.domain.PetitDejeuner import PetitDejeuner, IngredientsPetitDejeuner
from src.domain.Entree import Entree, IngredientsEntree
from src.domain.Dessert import Dessert, IngredientsDessert
from src.domain.Encas import Encas, IngredientsEncas
from src.domain.Vinaigrette import Vinaigrette, IngredientsVinaigrette
from src.domain.Menu import Menu
from itertools import product



def load_ciqual(df):
    """
    Load data from Ciqual.csv into the Ciqual table.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        ciqual = Ciqual(
            alim_grp_code=row['alim_grp_code'],
            alim_ssgrp_code=row['alim_ssgrp_code'],
            alim_ssssgrp_code=row['alim_ssssgrp_code'],
            rayon=row['rayon'],
            alim_code=row['alim_code'],
            alim_nom_fr=row['alim_nom_fr'],
            energieKj=row['energieKj'],
            energieKcal=row['energieKcal'],
            fibres=row['fibres'],
            calcium=row['calcium'],
            cuivre=row['cuivre'],
            fer=row['fer'],
            iode=row['iode'],
            magnesium=row['magnesium'],
            manganese=row['manganese'],
            phosphore=row['phosphore'],
            potassium=row['potassium'],
            selenium=row['selenium'],
            sodium=row['sodium'],
            zinc=row['zinc'],
            vitamineA=row['vitamineA'],
            vitamineD=row['vitamineD'],
            vitamineE=row['vitamineE'],
            vitamineK1=row['vitamineK1'],
            vitamineC=row['vitamineC'],
            vitamineB1=row['vitamineB1'],
            vitamineB2=row['vitamineB2'],
            vitamineB3=row['vitamineB3'],
            vitamineB5=row['vitamineB5'],
            vitamineB6=row['vitamineB6'],
            vitamineB9=row['vitamineB9'],
            vitamineB12=row['vitamineB12']
        )
        db.session.add(ciqual)
    db.session.commit()

def load_plats(df):
    """
    Load data from the DataFrame into the Plat and IngredientsPlat tables.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        if index + 2 not in [2, 15, 16, 35, 48, 49, 67, 80, 81, 99, 111, 112, 131, 144, 145, 163, 173, 176, 177, 219, 238, 242, 246, 262, 284, 343, 393, 473, 482, 499, 521, 531, 535, 556, 560, 563]:
            plat = Plat(
                id=row['Identifiant'],
                num_plat=row['NumPlat'],
                aliment=row['Aliment'],
                nom_groupe_plat=row['NomGroupePlat'],
                nom_famille_plat=row['NomFamPlat'],
                recette=row['TextRecette'],
                contient_viande=oui_non_to_bool(row['Viande']),
                contient_poisson=oui_non_to_bool(row['Poisson']),
                indice_glycemique=row['Ig(bas:55 ou moins; moyen: 56-60 élevé: >ou=70)'],
                macro_nutriment=row['MacroN'],
                est_vegetarien=oui_non_to_bool(row['Végé']),
                contient_gluten=oui_non_to_bool(row['sansGluten']),
                est_cetogene=oui_non_to_bool(row['cétogène']),
                duree_preparation=row['DurPrep'],
                debut_saison=row['SaisDeb'],
                fin_saison=row['SaisFin'],
                prix=row['Prix'],
                difficulte=row['Diff'],
                est_mediterraneen=oui_non_to_bool(row['Medi']),
                sans_sel=row['Sanssel'],
                contient_porc=oui_non_to_bool(row['Porc'])
            )
            plat.save_to_db()
            # Adding ingredients
            for i in range(1, 21): 
                ingredient_col = f'NumIng{i}'
                quantity_col = f'QteIng{i}'
                unit_col = f'UniteIng{i}'
                if pd.notna(row[ingredient_col]) and pd.notna(row[quantity_col]) and pd.notna(row[unit_col]):
                    query = IngredientsPlat.insert().values(
                        plat_id=plat.id,
                        ingredient_id=row[ingredient_col],
                        ingredient_quantité=row[quantity_col],
                        ingredient_unité=row[unit_col]
                    )
                    db.session.execute(query)
    
    db.session.commit()

def load_petits_dejeuners(df):
    """
    Load data from the DataFrame into the PetitDejeuner and IngredientsPetitDejeuner tables.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        petit_dejeuner = PetitDejeuner(
            id=row['Identifiant'],
            nom_famille_petit_dejeuner=row['NomFamPetitDejeuner'],
            recette=row['TextRecette'],
            contient_viande=oui_non_to_bool(row['Viande']),
            contient_poisson=oui_non_to_bool(row['Poisson']),
            indice_glycemique=row['Ig(bas:55 ou moins; moyen: 56-60 élevé: >ou=70)'],
            macro_nutriment=row['MacroN'],
            duree_preparation=row['DurPrep'],
            debut_saison=row['SaisDeb'],
            fin_saison=row['SaisFin'],
            prix=row['Prix'],
            difficulte=row['Diff'],
            est_mediterraneen=oui_non_to_bool(row['Medi']),
            sans_sel=row['Sanssel'],
            contient_porc=oui_non_to_bool(row['Porc']),
            gout=row['Goût'],
        )
        petit_dejeuner.save_to_db()
        # Adding ingredients
        for i in range(1, 16):
            ingredient_col = f'NumIng{i}'
            quantity_col = f'QteIng{i}'
            unit_col = f'UniteIng{i}'
            if pd.notna(row[ingredient_col]) and pd.notna(row[quantity_col]) and pd.notna(row[unit_col]):
                query = IngredientsPetitDejeuner.insert().values(
                    petit_dejeuner_id=petit_dejeuner.id,
                    ingredient_id=row[ingredient_col],
                    ingredient_quantité=row[quantity_col],
                    ingredient_unité=row[unit_col]
                )
                db.session.execute(query)

    db.session.commit()

def load_entrees(df):
    """
    Load data from the DataFrame into the Entree and IngredientsEntree tables.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        if index + 2 not in [8, 54]:
            entree = Entree(
                id=row['Identifiant'],
                nom_famille_entree=row['NomFamEntree'],
                recette=row['TextRecette'],
                contient_viande=oui_non_to_bool(row['Viande']),
                contient_poisson=oui_non_to_bool(row['Poisson']),
                indice_glycemique=row['Ig(bas:55 ou moins; moyen: 56-60 élevé: >ou=70)'],
                macro_nutriment=row['MacroN'],
                duree_preparation=row['DurPrep'],
                debut_saison=row['SaisDeb'],
                fin_saison=row['SaisFin'],
                prix=row['Prix'],
                difficulte=row['Diff'],
                est_mediterraneen=oui_non_to_bool(row['Medi']),
                sans_sel=row['Sanssel'],
                contient_porc=oui_non_to_bool(row['Porc'])
            )
            entree.save_to_db()
            # Adding ingredients
            for i in range(1, 16):
                ingredient_col = f'NumIng{i}'
                quantity_col = f'QteIng{i}'
                unit_col = f'UniteIng{i}'
                if pd.notna(row[ingredient_col]) and pd.notna(row[quantity_col]) and pd.notna(row[unit_col]):
                    query = IngredientsEntree.insert().values(
                        entree_id=entree.id,
                        ingredient_id=row[ingredient_col],
                        ingredient_quantité=row[quantity_col],
                        ingredient_unité=row[unit_col]
                    )
                    db.session.execute(query)

    db.session.commit()

def load_desserts(df):
    """
    Load data from the DataFrame into the Dessert and IngredientsDessert tables.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        dessert = Dessert(
            id=row['Identifiant'],
            nom_famille_dessert=row['NomFamDessert'],
            recette=row['TextRecette'],
            contient_viande=oui_non_to_bool(row['Viande']),
            contient_poisson=oui_non_to_bool(row['Poisson']),
            indice_glycemique=row['Ig(bas:55 ou moins; moyen: 56-60 élevé: >ou=70)'],
            macro_nutriment=row['MacroN'],
            duree_preparation=row['DurPrep'],
            debut_saison=row['SaisDeb'],
            fin_saison=row['SaisFin'],
            prix=row['Prix'],
            difficulte=row['Diff'],
            est_mediterraneen=oui_non_to_bool(row['Medi']),
            sans_sel=row['Sanssel'],
            contient_porc=oui_non_to_bool(row['Porc'])
        )
        dessert.save_to_db()
        # Adding ingredients
        for i in range(1, 16):
            ingredient_col = f'NumIng{i}'
            quantity_col = f'QteIng{i}'
            unit_col = f'UniteIng{i}'
            if pd.notna(row[ingredient_col]) and pd.notna(row[quantity_col]) and pd.notna(row[unit_col]):
                query = IngredientsDessert.insert().values(
                    dessert_id=dessert.id,
                    ingredient_id=row[ingredient_col],
                    ingredient_quantité=row[quantity_col],
                    ingredient_unité=row[unit_col]
                )
                db.session.execute(query)

    db.session.commit()

def load_encas(df):
    """
    Load data from the DataFrame into the Encas and IngredientsEncas tables.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        encas = Encas(
            id=row['Identifiant'],
            nom_famille_encas=row['NomFamEncas'],
            contient_viande=oui_non_to_bool(row['Viande']),
            contient_poisson=oui_non_to_bool(row['Poisson']),
            indice_glycemique=row['Ig(bas:55 ou moins; moyen: 56-60 élevé: >ou=70)'],
            macro_nutriment=row['MacroN'],
            duree_preparation=row['DurPrep'],
            debut_saison=row['SaisDeb'],
            fin_saison=row['SaisFin'],
            prix=row['Prix'],
            difficulte=row['Diff'],
            est_mediterraneen=oui_non_to_bool(row['Medi']),
            sans_sel=row['Sanssel'],
            contient_porc=oui_non_to_bool(row['Porc'])
        )
        encas.save_to_db()
        # Adding ingredients
        for i in range(1, 16):
            ingredient_col = f'NumIng{i}'
            quantity_col = f'QteIng{i}'
            unit_col = f'UniteIng{i}'
            if pd.notna(row[ingredient_col]) and pd.notna(row[quantity_col]) and pd.notna(row[unit_col]):
                query = IngredientsEncas.insert().values(
                    encas_id=encas.id,
                    ingredient_id=row[ingredient_col],
                    ingredient_quantité=row[quantity_col],
                    ingredient_unité=row[unit_col]
                )
                db.session.execute(query)

    db.session.commit()

def load_vinaigrette(df):
    """
    Load data from the DataFrame into the Vinaigrette and IngredientsVinaigrette tables.

    Args:
        df: The pandas DataFrame containing the data to load.
    """
    for index, row in df.iterrows():
        vinaigrette = Vinaigrette(
            id=row['Identifiant'],
            nom_famille_vinaigrette=row['NomFamVinaigrette'],
            recette=row['TextRecette']
        )
        vinaigrette.save_to_db()
        # Adding ingredients
        for i in range(1, 10):
            ingredient_col = f'NumIng{i}'
            quantity_col = f'QteIng{i}'
            unit_col = f'UniteIng{i}'
            if pd.notna(row[ingredient_col]) and pd.notna(row[quantity_col]) and pd.notna(row[unit_col]):
                query = IngredientsVinaigrette.insert().values(
                    vinaigrette_id=vinaigrette.id,
                    ingredient_id=row[ingredient_col],
                    ingredient_quantité=row[quantity_col],
                    ingredient_unité=row[unit_col]
                )
                db.session.execute(query)

    db.session.commit()

def load_menus(entrees_file, plats_file, desserts_file):
    """
    Load data from the DataFrame into the Menu table.

    Args:
        entrees_file: The pandas DataFrame containing the entree data.
        plats_file: The pandas DataFrame containing the plat data.
        desserts_file: The pandas DataFrame containing the dessert data to load.
    """
    # Commiting by batches is necessary to reduce memory usage	
    batch_size = 1000
    not_included_plat_id = [1, 14, 15, 34, 47, 48, 66, 79, 80, 98, 110, 111, 130, 143, 144, 162, 172, 175, 176, 218, 237, 241, 245, 261, 283, 342, 392, 472, 481, 498, 520, 530, 534, 555, 559, 562]
    not_included_entree_id = [7, 53]
    entrees_count = len(entrees_file)
    plats_count = len(plats_file)
    desserts_count = len(desserts_file)
    menu_combinations = product(
        [i for i in range(1, entrees_count + 1) if i not in not_included_entree_id],
        [i for i in range(1, plats_count + 1) if i not in not_included_plat_id],
        range(1, desserts_count + 1)
    )
    menu_id = 1

    for entree_id, plat_id, dessert_id in menu_combinations:
        menu = Menu(
            id=menu_id,
            entree_id=entree_id,
            plat_id=plat_id,
            dessert_id=dessert_id
        )
        db.session.add(menu)
        menu_id += 1

        # Commit in batches to manage memory usage
        if menu_id % batch_size == 0:
            db.session.commit()

    # Final commit for any remaining records
    db.session.commit()

# Mapping function to convert 'Oui'/'Non' to True/False
def oui_non_to_bool(value):

    if value == "oui":
        return True
    elif value == "non":
        return False
    else:
        raise Exception("Invalid boolean value")