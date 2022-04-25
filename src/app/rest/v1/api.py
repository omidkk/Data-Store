import logging

from flask import Blueprint, jsonify

_log = logging.getLogger(__name__)
api = Blueprint("api", __name__)


@api.route("/version", methods=["GET"])
def version():
    return jsonify(version="1.0")


@api.route("/health", methods=["GET"])
def health():
    return jsonify({"success": True, "app": "Data store challange"}), 200, {"ContentType": "application/json"}
