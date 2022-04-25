import pickle
import uuid
from pathlib import Path


class StoreAndRetrieveAsFileToLocal:
    def __init__(self):
        self.store_folder = Path("src/data_storage")
        self.retrieve_folder = Path("src/data_storage")

    def store(self, data):
        id = uuid.uuid4()
        file_to_open = self.store_folder / f"{id}.pkl"
        output = open(file_to_open, "wb")
        pickle.dump(data, output, protocol=pickle.HIGHEST_PROTOCOL)
        return id

    def retrieve(self, data_ids):
        all_data = {}
        for data_id in data_ids:
            file_to_open = self.retrieve_folder / f"{data_id}.pkl"
            data_as_file = open(file_to_open, "rb")
            data = pickle.load(data_as_file)
            all_data[data_id] = data
        return all_data
