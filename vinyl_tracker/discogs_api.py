from dotenv import load_dotenv
import requests
import discogs_client
import os
from vinyl_tracker.vinyl_state import VinylState
import logging

_logger = logging.getLogger(__name__)

class DiscogsAPI:
    def __init__(self):
        load_dotenv()
        self.__base_price_url = "https://api.discogs.com/marketplace/price_suggestions/{}"
        self.__pat = os.getenv('DISCOGS_PAT') or self._raise_env_error(
            'DISCOGS_PAT'
        )
        self.__key = os.getenv(
            'CONSUMER_KEY_DISCOGS'
        ) or self._raise_env_error('CONSUMER_KEY_DISCOGS')
        self.__secret = os.getenv('CONSUMER_SECRET_DISCOGS') or self._raise_env_error(
            'CONSUMER_SECRET_DISCOGS'
        )
        self.__req_token_url = os.getenv('REQ_TOKEN_DISCOGS') or self._raise_env_error(
            'REQ_TOKEN_DISCOGS'
        )
        self.__auth_url = os.getenv('AUTH_URL_DISCOGS') or self._raise_env_error(
            'AUTH_URL_DISCOGS'
        )
        self.__access_token_url = os.getenv('ACCESS_TOKEN_URL_DISCOGS') or self._raise_env_error(
            'ACCESS_TOKEN_URL_DISCOGS'
        )
        self.client = None
        self.__create_client_conection()

    def __create_client_conection(self):
        self.client = discogs_client.Client('Vinyl_Tracker/1.0', user_token=self.__pat)        
        self.id = self.client.identity()

    def get_price(self, id: int, state: VinylState):
        try:
            vinyl = self.client.release(id)
            price_obj = getattr(vinyl.price_suggestions, state.value())
            return price_obj
        except Exception as e:
            _logger.warning(f"Error fetching price for Vinyl {id}: {e}")

    def get_sale_qty(self, id: int):
        try:
            vinyl = self.client.release(id)
            qty = vinyl.marketplace_stats.num_for_sale
            return qty
        except Exception as e:
            _logger.warning(f"Error fetching marketplace stats for Vinyl {id}: {e}")


    def find_release_id(self, artist: str, title: str, year: int) -> int | None:
        format = "Vinyl"
        try:
            return self.client.search(artist=artist,title=title)
        except Exception as e:
            print(f"Error caught: {e}")

    def _raise_env_error(self, varname: str):
        """
        Raises a ValueError if a required environment variable is not set.

        Args:
            varname (str): Name of the missing environment variable.

        Raises:
            ValueError: If the environment variable is not defined.
        """
        raise ValueError(f"Variable {varname} not defined in .env file!")