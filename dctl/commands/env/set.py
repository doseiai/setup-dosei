import click
import requests

from dctl.utils.params import owner_params
from dctl.utils.session import get_auth_header
from dotenv import dotenv_values

from dctl.config import Config

config = Config()


@click.command()
@click.option('--file', default=".env")
@click.option('--owner', required=True)
@click.option('--yes', is_flag=True, default=False)
@click.argument('name', nargs=1, default=None, required=False)
@click.argument('value', nargs=1, default=None, required=False)
def set(file, owner, yes, name, value):
    """Set environment variables"""

    # Check if the name is provided.
    # $ dplex env set MY_ENV_VAR_NAME my_env_var_value
    if name:
        if value is None:
            raise click.UsageError("Missing argument 'VALUE'.")
        click.echo(f'Name:{name} Value: {value}')
        return

    # Load the environment variables from the .env file
    env_variables = dotenv_values(file)
    params = owner_params(owner)

    # Prompt user before loading environment variables from env file, if yes mode is off
    if not yes:
        click.confirm('Load environment variables from .env file?', abort=True)

    # Send a POST request to the API with the environment variables as JSON
    headers = {**get_auth_header()}
    response = requests.post(f"{config.api_base_url}/envs", params=params, json=env_variables, headers=headers)
    env_variables = response.json()
    names = [env_variable.get("name") for env_variable in env_variables]
    click.echo(f"Success! Environment variables {', '.join(names)} have been updated successfully.")
