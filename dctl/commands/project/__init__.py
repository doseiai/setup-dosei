import click
from dctl.commands.project.list import list


@click.group("project", help="Project commands")
def project():
    pass


project.add_command(list)
