import json

import click
import requests

from deployplex.config import Config
from deployplex.utils.params import owner_params
from deployplex.utils.session import get_auth_header

config = Config()


def display_table(headers, header_names, rows):
    # Determine the maximum width of each column
    column_widths = [len(header) for header in header_names]
    for row in rows:
        for i, header in enumerate(headers):
            cell = row[header]
            column_widths[i] = max(column_widths[i], len(str(cell)))

    # Print the table
    formatted_headers = [header.ljust(width) for header, width in zip(header_names, column_widths)]
    click.echo('   '.join(formatted_headers))
    for row in rows:
        formatted_row = [str(row[header]).ljust(width) for header, width in zip(headers, column_widths)]
        click.echo('   '.join(formatted_row))


@click.command()
@click.option('--owner', default=None, required=True)
@click.option("--json", "json_output", is_flag=True, default=False)
def list(owner, json_output):
    """List secrets"""
    auth_header = get_auth_header()
    params = owner_params(owner)
    result = requests.get(f"{config.api_base_url}/secrets", headers=auth_header, params=params)
    headers = ["name", "updated_at"]
    header_names = ["NAME", "LAST UPDATE"]
    rows = result.json()
    if json_output:
        return click.echo(json.dumps(rows))
    display_table(headers, header_names, rows)
