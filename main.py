from okcupid.api import OkCupidClient  # noqa E402
from okcupid.logger import setup_logger
import click


@click.command()
@click.option("--msg", type=str, default="Hello World!", help="sample message to send for testing")
def cli(msg: str):
    logger = setup_logger(__name__)
    client = OkCupidClient()
    client.stack_menu_query()
    for i in range(min(client.likes_remaining, len(client.stack_matches))):
        target_user = client.stack_matches[i]
        client.send_msg(target_user, msg)


if __name__ == '__main__':
    cli()
