import os
from pathlib import Path

import pytest

from src.data_store.store_retrieve_json import StoreAndRetrieveJsonAsFileToLocal


@pytest.fixture
def test_input_1():
    data = [{"omid": 1376}, {"test": "test"}]

    return data


@pytest.fixture
def test_input_2():
    data = [{"amir": 1576}, {"amount": 5.8}]

    return data


def test_store(test_input_1):
    store_obj = StoreAndRetrieveJsonAsFileToLocal()
    data_id = store_obj.store(test_input_1)
    assert os.path.exists(Path(f"src/data_store/data_storage/{data_id}.pkl"))
    os.remove(Path(f"src/data_store/data_storage/{data_id}.pkl"))


def test_retrieve(test_input_1, test_input_2):
    retrieve_obj = StoreAndRetrieveJsonAsFileToLocal()
    data_id_1 = retrieve_obj.store(test_input_1)
    read_data = retrieve_obj.retrieve([data_id_1])
    assert read_data == test_input_1

    data_id_2 = retrieve_obj.store(test_input_2)
    read_data = retrieve_obj.retrieve([data_id_2])
    assert read_data == test_input_2

    read_data = retrieve_obj.retrieve([data_id_1, data_id_2])
    assert read_data == test_input_1 + test_input_2

    os.remove(Path(f"src/data_store/data_storage/{data_id_1}.pkl"))
    os.remove(Path(f"src/data_store/data_storage/{data_id_2}.pkl"))
