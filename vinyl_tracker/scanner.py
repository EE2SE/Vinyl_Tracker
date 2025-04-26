from vinyl_tracker.discogs_api import DiscogsAPI
from vinyl_tracker.vinyl_db import VinylDB


class Subject:
    """Represents what is being observed"""

    def __init__(self):
        """create an empty observer list"""

        self._observers = []

    def notify(self, modifier=None):
        """Alert the observers"""

        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        """If the observer is not in the list,
        append it into the list"""

        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """Remove the observer from the observer list"""

        try:
            self._observers.remove(observer)
        except ValueError:
            pass


class VinylScanner(Subject):
    """
    will scan and notify the upater
    """

    def __init__(self, api: DiscogsAPI, db_engine: VinylDB):
        self._api = api
        self._db_engine = db_engine
        pass
