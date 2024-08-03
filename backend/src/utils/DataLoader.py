import logging
from src.DatabaseConfig import db
from pathlib import Path
import pandas as pd
from sqlalchemy import text
from src.utils.Loaders import load_ciqual, load_plats, load_petits_dejeuners, load_encas, load_desserts, load_entrees, load_vinaigrette, load_menus


def load_data(app):
    """
    Load data from CSV files into the database tables.

    Args:
        app: The Flask application instance.
    """
    with app.app_context():
        # Define paths to the directories containing the data CSV files
        base_path = Path(__file__).resolve().parent
        data_location = base_path / "data"
        # List of tables and corresponding CSV files to load, loader represents the function that loads the file's data
        data_load_object = [
            {"table": "Ciqual", "file": "Ciqual.csv", "file_location": data_location, "loader": load_ciqual},
            {"table": "Plat", "file": "Plats.csv", "file_location": data_location, "loader": load_plats},
            {"table": "PetitDejeuner", "file": "PetitsDejeuners.csv", "file_location": data_location, "loader": load_petits_dejeuners},
            {"table": "Entree", "file": "Entrees.csv", "file_location": data_location, "loader": load_entrees},
            {"table": "Encas", "file": "Encas.csv", "file_location": data_location, "loader": load_encas},
            {"table": "Dessert", "file": "Desserts.csv", "file_location": data_location, "loader": load_desserts},
            {"table": "Vinaigrette", "file": "Vinaigrettes.csv", "file_location": data_location, "loader": load_vinaigrette},
            {"table": "Menu", "file":"", "file_location": data_location, "loader": load_menus},
        ]

        # Iterate through the data load objects
        for data_load in data_load_object:
            table_name = data_load["table"]
            logging.info(f"Checking data load for {table_name}")

            try:
                if (app.config["FLASK_ENV"] == "production"):
                    query = f"SELECT EXISTS (SELECT * FROM \"{table_name}\")"
                else:
                    query = f"SELECT count(1) FROM {table_name}"
                
                # Check if the table is empty
                result = db.session.execute(
                    text(query)
                ).scalar()
                
                if result < 1:
                    if data_load["file"]:
                        data_file = data_load["file_location"] / data_load["file"]
                        if data_file.is_file():
                            logging.info(
                                f"Loading data file {data_file} to table {table_name}"
                            )
                            df = pd.read_csv(data_file)
                            data_load["loader"](df)
                            logging.info(f"Data loaded successfully into {table_name}")
                        else:
                            logging.warning(f"Data file {data_file} does not exist")
                    else:
                        # For loaders that doesn't need a file
                        logging.info(
                            f"Loading data for to table {table_name}"
                        )
                        entrees_file =  pd.read_csv(data_load["file_location"] / "Entrees.csv")
                        plats_file =  pd.read_csv(data_load["file_location"] / "Plats.csv")
                        desserts_file =  pd.read_csv(data_load["file_location"] / "Desserts.csv")
                        data_load["loader"](entrees_file, plats_file, desserts_file)
                else:
                    logging.info(
                        f"{table_name} is already populated. Skipping data load..."
                    )
            except Exception as e:
                logging.error(f"Error loading data for table {table_name}: {e}")
