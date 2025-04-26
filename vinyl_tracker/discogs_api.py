from vinyl_tracker.config import APIConfig


class DiscogsAPI:
    def __init__(self, config: APIConfig):
        self._config = config
