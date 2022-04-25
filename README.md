# Data-Store
This project contains a api to store, or retrieve data.

#### Technologies
- python 3

#### Prerequisites
- Install packages defined in requirements.txt

#### Docs

Postman Collection is available in the src->docs

#### Apis

The project currently supports the storing Json data in the local, with pickle format. 
```
POST {{base_url}}/data/operations
```
Simple body:
```
{
    "format": "json",
    "destination": "local",
    "content":[
        {"omid":1376},
        {"azar":1363}
    ]
}
```
Content could include list of Jsons.

The project support the Json retrieve from local storage.
```
GET {{base_url}}/data/operations
```
Simple body:
```
{
    "format": "json",
    "destination": "local",
    "data_ids": ["23f5c02a-de0c-4985-a821-7405e1051f6a"]
}
```
The data_ids could include list of files, to get multiple data with one request.
This api also supports offset, and limit as query parameters.

#### Test
```
$ pytest src/data_store/test/json_local_store_test.py
```
Tests the data store/retrieve. 

#### Note
Data store could be published as separated library.