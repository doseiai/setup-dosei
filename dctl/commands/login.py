import threading
import webbrowser
import click
import requests

from dctl.config import Config
from dctl.schemas.session import SessionCredentials
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

config = Config()
AUTH_URL = f"https://github.com/login/oauth/authorize?client_id={config.github_client_id}&redirect_uri=http://localhost:8085/auth/github/cli&scope=read:user,user:email"


class AuthHandler(BaseHTTPRequestHandler):
    succeeded = False

    def log_message(self, format, *args):
        """Override to prevent default logging."""
        pass

    def do_GET(self):
        """Handle GET request."""
        # Parse the request URL
        parsed_url = urlparse(self.path)
        if parsed_url.path == "/auth/github/cli":
            query_params = parse_qs(parsed_url.query)
            if 'code' in query_params:
                # Extract the code from the callback URL
                response = requests.get(f"{config.api_base_url}/auth/github/cli", params={"code": query_params['code'][0]})
                config.store_token_from_session(SessionCredentials(**response.json()))
                AuthHandler.succeeded = True
                self.send_response(302)
                self.send_header('Location', 'https://dosei.ai/login/cli')
                self.end_headers()
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Authentication failed!")
            # Shut down the server
            self.server.shutdown()


@click.command()
def login():
    """Authenticate with a Dosei"""
    # Spin up an HTTP server
    server = ThreadingHTTPServer(('localhost', 8085), AuthHandler)

    # Use a separate thread to run the server
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()

    # Open the browser for authentication
    webbrowser.open(AUTH_URL)

    click.echo(f"Your browser has been opened to visit:\n\n{AUTH_URL}\n")

    # Wait for the server thread to finish (i.e., when the server shuts down)
    server_thread.join()

    if AuthHandler.succeeded:
        click.echo("Login Succeeded!")
    else:
        click.echo("Login Failed!")
