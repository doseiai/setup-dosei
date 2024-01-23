import click
import requests

from dctl.config import Config
from dctl.utils.session import get_auth_header

config = Config()


@click.command()
def logout():
    """Remove Authentication with a Dosei"""
    session = config.session()
    headers = {**get_auth_header()}
    url = f"{config.api_base_url}/auth/logout"
    request = requests.delete(url, headers=headers, params={"session_id": session.id})
    request.raise_for_status()
    config.remove_stored_credentials()
    click.echo("Logout Succeeded!")
