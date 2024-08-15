import pytest
from okcupid import consts
from okcupid.api import OkCupidClient

@pytest.fixture(scope="module")
def stack_data_query_data() -> str:
    with open(consts.RESOURCES_DIR / "stack_menu_query.json") as stack_menu_query_fd:
        return stack_menu_query_fd.read()


@pytest.fixture(scope="function")
def client() -> OkCupidClient:
    return OkCupidClient()
