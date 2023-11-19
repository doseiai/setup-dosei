import json
import os
from dctl.schemas.session import SessionCredentials


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

        self._credentials_path = os.path.expanduser('~/.dosei/credentials.json')
        self._token = os.getenv("DOSEI_TOKEN")

        self.api_base_url = os.getenv("API_BASE_URL", "https://api.dosei.ai")
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

    def remove_stored_credentials(self) -> bool:
        """"
        Remove credentials file
        """
        os.remove(self._credentials_path)
        return True

    def session(self) -> SessionCredentials | None:
        if os.path.isfile(self._credentials_path) is False:
            return None
        with open(self._credentials_path, 'r') as file:
            credentials = SessionCredentials(**json.load(file))
            return credentials

    def session_token(self) -> str | None:
        """
        Get session token

        Use self.token if set, if not set, use ~/.dosei/credentials.json
        """
        if self._token:
            return self._token

        if os.path.isfile(self._credentials_path) is False:
            return None
        with open(self._credentials_path, 'r') as file:
            credentials = SessionCredentials(**json.load(file))
            return credentials.token
