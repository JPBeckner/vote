from os import path
from logging.config import dictConfig
from json import load

from dotenv import load_dotenv
from falcon.app import App
from wsgiref.simple_server import make_server

from src.domain.services.vote_service import RegistryVoteImpl
from src.adapter.sqlite.output.repository import RepositoryImpl
from src.adapter.falcon.input.vote_controler import VoteController


# TO DO: create checkpoint Service


def config_logging():
    log_config_path = path.join(
        path.dirname(__file__),
        '../log-config.json'
    )
    with open(log_config_path) as file:
        dict_config = load(file)
    dictConfig(dict_config)


if __name__ == "__main__":

    load_dotenv()
    config_logging()
    
    repo = RepositoryImpl()
    service = RegistryVoteImpl(repo=repo)

    app = App()
    app.add_route("/vote/{code:int}", VoteController(service=service))
    with make_server('0.0.0.0', 8000, app) as httpd:
        print('Serving on port 8000...')

        # Serve until process is killed
        httpd.serve_forever()

