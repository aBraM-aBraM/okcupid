from okcupid.api import OkCupidClient  # noqa E402

if __name__ == '__main__':
    client = OkCupidClient()
    client.stack_menu_query()
    target_user = client.stack_matches[0]
    client.send_msg(target_user, "Hello World!")
