from enum import Enum

import click
import requests
from pydantic import BaseModel

from dctl.config import Config
from dctl.utils.session import get_auth_header

config = Config()


class Template(BaseModel):
    source_full_name: str
    path: str
    branch: str


class TemplateType(Enum):
    FASTAPI = Template(source_full_name="doseiai/dosei", path="examples/fastapi", branch="main")


@click.command()
@click.option(
    '--template',
    default="fastapi",
    type=click.Choice(['fastapi'], case_sensitive=False),
    required=True
)
@click.argument('name', nargs=1, default=None, required=True)
def new(template, name):
    """New project"""
    headers = {**get_auth_header()}
    url = f"{config.api_base_url}/projects/test/clone"
    response = requests.post(url, headers=headers, json={
        "name": name,
        **TemplateType[template.upper()].value.model_dump()
    })
    response.raise_for_status()
