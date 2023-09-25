import json
import os
from deployplex.schemas.session import SessionCredentials


class Config:
    _self = None
    _initialized = False

    def __new__(cls):
        if cls._self is None:
            cls._self = super(Config, cls).__new__(cls)
        return cls._self

    def __init__(self):
        if self._initialized:
            return

        self._credentials_path = os.path.expanduser('~/.dplex/credentials.json')
        self._token = os.getenv("DEPLOYPLEX_TOKEN")

        self.api_base_url = os.getenv("API_BASE_URL", "https://api.deployplex.com")
        self.github_client_id = "Iv1.0d2388105db85287"

        self._initialized = True

    def store_token_from_session(self, session: SessionCredentials) -> bool:
        """
        Store the access token in the credentials file.

        return True if credentials stored.
        """

        # Store the access token in the credentials file
        os.makedirs(os.path.dirname(self._credentials_path), exist_ok=True)
        with open(self._credentials_path, 'w') as f:
            json.dump(session.model_dump(), f, indent=2)
        return True

    def session_token(self) -> str:
        """
        Get session token

        Use self.token if set, if not set, use ~/.dplex/credentials.json
        """
        return self._token