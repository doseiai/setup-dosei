import json

import click
import requests

from dctl.config import Config
from dctl.utils.params import owner_params
from dctl.utils.session import get_auth_header

config = Config()


@click.command()
@click.option('--owner', default=None, required=True)
@click.option('--format', default=None, required=False, type=click.STRING)
def list(owner, format):
    """List environment variables"""
    auth_header = get_auth_header()
    params = owner_params(owner)
    result = requests.get(f"{config.api_base_url}/envs", headers=auth_header, params=params)
    rows = result.json()
    if format is None:
        for row in rows:
            click.echo(f'{row.get("name")}={row.get("value")}')
    elif format == "json":
        return click.echo(json.dumps(rows))
    else:
        raise click.ClickException("Invalid format")
