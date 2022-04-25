import pickle
import uuid
from pathlib import Path


class StoreAndRetrieveJsonAsFileToLocal:
    def __init__(self):
        self.store_folder = Path("src/data_store/data_storage/")
        self.retrieve_folder = Path("src/data_store/data_storage/")

    def store(self, data):
        data_id = uuid.uuid4()
        file_to_open = self.store_folder / f"{data_id}.pkl"
        with open(file_to_open, "wb") as output:
            pickle.dump(data, output, protocol=pickle.HIGHEST_PROTOCOL)
        return data_id

    def retrieve(self, data_ids):
        data = []
        for data_id in data_ids:
            file_to_open = self.retrieve_folder / f"{data_id}.pkl"
            try:
                with open(file_to_open, "rb") as data_as_file:
                    data += pickle.load(data_as_file)
            except FileNotFoundError:
                pass
        return data


class StoreAndRetrieveJsonAsFileToS3:
    def __init__(self):
        pass

    def store(self, data):
        pass

    def retrieve(self, data_ids):
        pass
