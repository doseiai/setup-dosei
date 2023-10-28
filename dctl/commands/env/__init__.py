import click
from dctl.commands.env.set import set
from dctl.commands.env.list import list


@click.group("env", help="Environment variables commands")
def env():
    pass


env.add_command(set)
env.add_command(list)
