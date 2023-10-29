import click
from dctl.commands.project.list import list
from dctl.commands.project.open import open


@click.group("project", help="Project commands")
def project():
    pass


project.add_command(list)
project.add_command(open)
