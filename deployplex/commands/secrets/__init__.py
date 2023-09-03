import click
from deployplex.commands.secrets.set import set
from deployplex.commands.secrets.list import list


@click.group("secrets", help="Secrets commands")
def secrets():
    pass


secrets.add_command(set)
secrets.add_command(list)
