import click
import requests

from dctl.config import Config
from dctl.utils.params import owner_params
from dctl.utils.session import get_auth_header
from requests.exceptions import HTTPError

config = Config()


@click.command()
@click.option('--owner', default=None, required=True)
def logs(owner):
    """Stream project logs from Dosei"""
    auth_header = get_auth_header()
    params = owner_params(owner)
    url = f"{config.api_base_url}/projects/{params['owner_name']}/{params['project_name']}/logs/stream"

    try:
        with requests.get(url, headers=auth_header, stream=True) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    click.echo(decoded_line)
    except HTTPError as e:
        if e.response.status_code == 404:
            raise click.ClickException("Project not found")
        else:
            raise
