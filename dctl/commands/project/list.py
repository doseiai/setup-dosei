from datetime import datetime

import click
import requests

from dctl.config import Config
from dctl.utils.session import get_auth_header

config = Config()


def display_table(headers, header_names, rows):
    column_widths = [len(header) for header in header_names]
    for row in rows:
        for i, header in enumerate(headers):
            cell = row.get(header, "")
            column_widths[i] = max(column_widths[i], len(str(cell)))

    formatted_headers = [header.ljust(width) for header, width in zip(header_names, column_widths)]
    click.echo('   '.join(formatted_headers))

    for row in rows:
        formatted_row = [str(row.get(header, "")).ljust(width) for header, width in zip(headers, column_widths)]
        click.echo('   '.join(formatted_row))


@click.command()
def list():
    """List projects"""
    auth_header = get_auth_header()
    user_result = requests.get(f"{config.api_base_url}/user", headers=auth_header)
    projects_result = requests.get(f"{config.api_base_url}/projects", headers=auth_header)

    headers = ["name", "updated_at"]
    header_names = ["Name", "Last Updated"]
    user = user_result.json()
    projects = projects_result.json()
    for project in projects:
        project['name'] = f"{user['username']}/{project['name']}"
        project["updated_at"] = datetime.strptime(project["updated_at"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d %b, %Y")
    display_table(headers, header_names, projects)
