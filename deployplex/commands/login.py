import click
from deployplex.config import Config
from deployplex.schemas.session import SessionCredentials

config = Config()
# AUTH_URL = f"https://github.com/login/oauth/authorize?client_id={config.github_client_id}&redirect_uri={config.api_base_url}/auth/github&scope=read:user,user:email"


@click.command()
def login():
    """Authenticate with a DeployPlex"""
    raise click.ClickException("Not implemented, use DEPLOYPLEX_TOKEN env variable instead.")

    # Open the browser for authentication
    # webbrowser.open(AUTH_URL)

    # Store the access token in the credentials file
    config.store_token_from_session(SessionCredentials(id="id_value", token="token_value", refresh_token="dff"))
    click.echo("Login Succeeded!")
