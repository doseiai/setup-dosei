import click
import requests

from deployplex.config import Config
from deployplex.utils.session import get_auth_header

config = Config()


@click.command()
def logout():
    """Remove Authentication with a DeployPlex"""
    session = config.session()
    headers = {**get_auth_header()}
    url = f"{config.api_base_url}/auth/logout"
    # TODO: Fix, seems like isn't working.
    requests.delete(url, headers=headers, params={"session_id": session.id})
    config.remove_stored_credentials()
    click.echo("Logout Succeeded!")
