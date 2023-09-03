import click
import requests

from deployplex.utils.params import owner_params
from deployplex.utils.session import get_auth_header
from dotenv import dotenv_values

from deployplex.config import Config

config = Config()


@click.command()
@click.option('--env-file', default=".env")
@click.option('--owner', required=True)
@click.option('--yes', is_flag=True, default=False)
@click.argument('name', nargs=1, default=None, required=False)
@click.argument('value', nargs=1, default=None, required=False)
def set(env_file, owner, yes, name, value):
    """Set secret"""

    # Check if the name is provided.
    # $ dplex secrets set MY_SECRET_NAME my_secret_value
    if name:
        if value is None:
            raise click.UsageError("Missing argument 'VALUE'.")
        click.echo(f'Name:{name} Value: {value}')
        return

    # Load the secrets from the .env file
    secrets = dotenv_values(env_file)
    params = owner_params(owner)

    # Prompt user before loading secrets from env file, if yes mode is off
    if not yes:
        click.confirm('Load secrets from .env file?', abort=True)

    # Send a POST request to the API with the secrets as JSON
    headers = {**get_auth_header()}
    response = requests.post(f"{config.api_base_url}/secrets", params=params, json=secrets, headers=headers)
    secrets = response.json()
    names = [secret.get("name") for secret in secrets]
    click.echo(f"Success! Secrets {', '.join(names)} have been updated successfully.")
