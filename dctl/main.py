import click
from dctl.commands.env import env
from dctl.commands.login import login
from dctl.commands.logout import logout
from dctl.commands.logs import logs
from dctl.commands.project import project
from dctl.config import Config

config = Config()


@click.group()
@click.version_option(None, *("-v", "--version"), package_name="dctl")
@click.help_option(*("-h", "--help"))
def cli():
    pass


cli.add_command(login)
cli.add_command(logout)
cli.add_command(logs)
cli.add_command(env)
cli.add_command(project)

if __name__ == '__main__':
    cli()
