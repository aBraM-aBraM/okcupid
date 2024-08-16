from okcupid import consts


def test_parse_stack_menu_query(stack_data_query_data, client):
    client.parse_stack_menu_query(stack_data_query_data)
    existing_stack_ids = [stack["id"] for stack in client._stacks]

    diff_stack_ids = set(consts.STACK_ORDER).difference(set(existing_stack_ids))

    stack_id_test_order = consts.STACK_ORDER
    for diff_stack_id in diff_stack_ids:
        stack_id_test_order.remove(diff_stack_id)

    for i, stack in enumerate(client._stacks):
        assert stack_id_test_order[i] == stack["id"]
