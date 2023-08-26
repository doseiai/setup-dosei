import click


@click.version_option(None, *("-v", "--version"), package_name="deployplex")
@click.help_option(*("-h", "--help"))
def cli():
    pass


if __name__ == '__main__':
    cli()
