from src.api import OkCupidClient
from src.logger import setup_logger
from src.cfg import config
from src import consts
import click
from pathlib import Path
import logging


@click.command()
@click.option(
    "--msg", type=str, default="Hello World!", help="sample message to send for testing"
)
@click.option(
    "--session",
    type=click.types.Path(exists=True, dir_okay=False),
    default=".session",
    help="okcupid session file",
)
def cli(msg: str, session: str):
    session = Path(session)

    config.load(consts.PROJECT_DIR / "okcupid.json")

    logger = setup_logger(__name__, config.get("log_dir"))
    logger.setLevel(logging.DEBUG)

    if not session.is_absolute():
        session = consts.PROJECT_DIR / session
    with open(session) as session_fd:
        session = session_fd.read().strip()

    client = OkCupidClient(session)
    client.stack_menu_query()
    for i in range(min(client.likes_remaining, len(client.stack_matches))):
        target_user = client.stack_matches[i]
        client.send_msg(target_user, msg)


if __name__ == "__main__":
    cli()
