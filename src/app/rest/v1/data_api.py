import logging

from flask import Blueprint, jsonify, request
from flask_paginate import Pagination, get_page_parameter

from src.app.service.store_service import StoreData

_log = logging.getLogger(__name__)
data_store = Blueprint("data", __name__)


@data_store.route("/operations", methods=["POST"])
def store():
    in_ = request.get_json()
    response = StoreData.store(in_["format"], in_["destination"], in_["content"])

    return jsonify(response[0]), response[1], {"ContentType": "application/json"}


@data_store.route("/operations", methods=["GET"])
def retrieve():
    in_ = request.get_json()
    response = StoreData.retrieve(in_["format"], in_["destination"], in_["data_ids"])
    data = response[0]
    status = response[1]

    if "limit" in request.args and "offset" in request.args:
        limit_ = int(request.args.get('limit'))
        offset_ = int(request.args.get('offset'))
        data = data[offset_:offset_+limit_:]

    return jsonify(data), status, {"ContentType": "application/json"}
