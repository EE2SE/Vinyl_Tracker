from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from vinyl_models import prod_models as pm
from dotenv import load_dotenv
import logging
import os

_logger = logging.getLogger(__name__)

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode=require"


class VinylDBBase:
    """
    Singleton class to manage a database connection using SQLAlchemy.

    Automatically loads environment variables based on the given environment,
    builds the connection string, and provides an SQLAlchemy session.

    Attributes:
        session (Session): SQLAlchemy session factory.
        engine (Engine): SQLAlchemy engine connected to the database.
    """

    __instance = None

    def __new__(cls, environment: str):
        """
        Ensures only one instance of VinylDB exists (Singleton pattern).

        Args:
            environment (str): The environment prefix (e.g., 'DEV', 'PROD').

        Returns:
            VinylDB: The single instance of the VinylDB class.
        """
        if cls.__instance is None:
            cls.__instance = super(VinylDB, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self, environment: str):
        """
        Initializes the VinylDB instance if not already initialized.

        Loads environment variables and establishes a database connection.

        Args:
            environment (str): The environment prefix (e.g., 'DEV', 'PROD').
        """
        if self.__initialized:
            return  # Skip reinitializing if already done

        load_dotenv()
        self.__env = environment
        self.__db_user_varname = f"{self.__env}_DB_USER"
        self.__db_password_varname = f"{self.__env}_DB_PASSWORD"
        self.__db_host_varname = f"{self.__env}_DB_HOST"
        self.__db_port_varname = f"{self.__env}_DB_PORT"
        self.__db_name_varname = f"{self.__env}_DB_NAME"

        self.__db_user = os.getenv(self.__db_user_varname) or self._raise_env_error(
            self.__db_user_varname
        )
        self.__db_password = os.getenv(
            self.__db_password_varname
        ) or self._raise_env_error(self.__db_password_varname)
        self.__db_host = os.getenv(self.__db_host_varname) or self._raise_env_error(
            self.__db_host_varname
        )
        self.__db_port = os.getenv(self.__db_port_varname) or self._raise_env_error(
            self.__db_port_varname
        )
        self.__db_name = os.getenv(self.__db_name_varname) or self._raise_env_error(
            self.__db_name_varname
        )

        self.session = None
        self.engine = None
        self._establish_connection()
        self.__initialized = True  # Mark as initialized

    def _establish_connection(self):
        """
        Establishes the database connection using SQLAlchemy.

        Creates an engine and a session factory.
        """
        conn_string = DATABASE_URL.format(
            self.__db_user,
            self.__db_password,
            self.__db_host,
            self.__db_port,
            self.__db_name,
        )
        self.engine = create_engine(conn_string)
        self.session: Session = sessionmaker(bind=self.engine)

    def _raise_env_error(self, varname: str):
        """
        Raises a ValueError if a required environment variable is not set.

        Args:
            varname (str): Name of the missing environment variable.

        Raises:
            ValueError: If the environment variable is not defined.
        """
        raise ValueError(f"Variable {varname} not defined in .env file!")


class VinylDB(VinylDBBase):
    def __init__(self, environment: str):
        super().__init__(environment)

    def add_new_listing(self):
        _logger.info("Adding new listing")
        pass

    def update_currency_exchange(self):
        _logger.info("Updating currency exchange")
        pass

    def update_total_availability(self):
        _logger.info("Updating total market availability")
        pass

    def add_record_to_vault(self):
        _logger.info("Adding new record to vault")
        pass

    def add_price_to_record(self):
        _logger.info("Adding new price info to record")
        pass

    def get_all_records_in_vault(self) -> list[pm.Record] | None:
        """
        Fetches all records from the database.

        Args:
            session (Session): SQLAlchemy session instance.

        Returns:
            List[Record]: List of all Record instances.
        """
        try:
            return self.session.query(pm.Record).all()
        except Exception as e:
            _logger.warning(f"Failed to fetch all records from Supabase: {e}")
