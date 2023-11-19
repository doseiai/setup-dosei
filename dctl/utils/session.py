import click

from dctl.config import Config

config = Config()


def get_auth_header():
    token = config.session_token()
    if token is None:
        raise click.ClickException(
            'To get started with Dosei CLI, please run: dctl login\n'
            'Alternatively, populate the DOSEI_TOKEN environment variable with a Dosei API authentication '
            'token.'
        )
    return {"Authorization": f"Bearer {token}"}
