import click
import os
import webbrowser
import configparser


@click.group("open", help="Project open commands")
def open():
    pass


@open.command(name="git", help="Open project git repository")
def open_git():
    git_config_path = os.path.join(os.getcwd(), '.git', 'config')

    if not os.path.exists(git_config_path):
        raise click.ClickException("No .git folder found.")

    config = configparser.ConfigParser()
    config.read(git_config_path)

    try:
        url = config.get('remote "origin"', 'url')
        if url.startswith("git@"):
            url = url.replace(":", "/").replace("git@", "https://").replace(".git", "")
        webbrowser.open(url)
    except configparser.NoSectionError:
        raise click.ClickException("Remote origin not found.")
    except Exception as e:
        raise click.ClickException(f"An error occurred: {e}")
