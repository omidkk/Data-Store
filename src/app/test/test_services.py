import pytest

from src.app.service.store_retrieve_service import StoreRetrieveData


@pytest.fixture
def test_store_input():
    return {"format": "json", "destination": "local", "content": [{"omid": 1376}, {"azar": 1363}]}


def test_store(test_store_input):
    response = StoreRetrieveData.store(
        test_store_input["format"], test_store_input["destination"], test_store_input["content"]
    )
    assert response[1] == 200


def test_retrieve(test_store_input):
    store_response = StoreRetrieveData.store(
        test_store_input["format"], test_store_input["destination"], test_store_input["content"]
    )
    data_id = store_response[0]["dataset_id"]
    retrieve_response = StoreRetrieveData.retrieve(
        test_store_input["format"], test_store_input["destination"], ["invalid"]
    )
    assert retrieve_response[1] == 204
    retrieve_response = StoreRetrieveData.retrieve(
        test_store_input["format"], test_store_input["destination"], [data_id]
    )
    assert retrieve_response[1] == 200
