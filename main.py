from okcupid.api import OkCupidClient 
from okcupid.logger import setup_logger
from okcupid.cfg import Config, config
from okcupid import consts
import click
import logging

@click.command()
@click.option("--msg", type=str, default="Hello World!", help="sample message to send for testing")
def cli(msg:  str):
    config.load(consts.PROJECT_DIR / "okcupid.json")

    logger = setup_logger(__name__, config.get("log_dir"))
    logger.setLevel(logging.DEBUG)
    
    client = OkCupidClient()
    client.stack_menu_query()
    for i in range(min(client.likes_remaining, len(client.stack_matches))):
        target_user = client.stack_matches[i]
        client.send_msg(target_user, msg)


if __name__ == '__main__':
    cli()
