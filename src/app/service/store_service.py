from src.data_store.store_retrieve_json import StoreAndRetrieveAsFileToLocal


class StoreData:
    @classmethod
    def store(cls, data_format, data_destination, data_content):
        if data_format == "json":
            if data_destination == "local":
                store_obj = StoreAndRetrieveAsFileToLocal()
                data_id = store_obj.store(data_content)
                return {"message": f"Data stored as Json in the Local with id: {data_id}"}, 200
        return {"message": "Data format, or destination is not supported!"}, 500

    @classmethod
    def retrieve(cls, data_format, data_destination, data_ids):
        if data_format == "json":
            if data_destination == "local":
                store_obj = StoreAndRetrieveAsFileToLocal()
                data = store_obj.retrieve(data_ids)
                return data, 200
        return {"Data format, or destination is not supported!"}, 500
