import logging

from flask import Blueprint, jsonify, request

from src.app.service.store_retrieve_service import StoreRetrieveData

_log = logging.getLogger(__name__)
data_store = Blueprint("data", __name__)


@data_store.route("/operations", methods=["POST"])
def store():
    in_ = request.get_json()
    response = StoreRetrieveData.store(in_["format"], in_["destination"], in_["content"])

    return jsonify(response[0]), response[1], {"ContentType": "application/json"}


@data_store.route("/operations", methods=["GET"])
def retrieve():
    in_ = request.get_json()
    response = StoreRetrieveData.retrieve(in_["format"], in_["destination"], in_["data_ids"])
    data = response[0]
    status = response[1]
    if "limit" in request.args and "offset" in request.args and data:
        limit_ = int(request.args.get("limit"))
        offset_ = int(request.args.get("offset"))
        data = data[offset_ : offset_ + limit_ :]
    return jsonify(data), status, {"ContentType": "application/json"}
