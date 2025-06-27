from flask import Blueprint, request, jsonify
from app.services.in_memory import redis_client

events_bp = Blueprint("events", __name__)

@events_bp.route("/", methods=["GET"])
def list_events():
    return jsonify({"events": []})  # Placeholder

@events_bp.route("/", methods=["POST"])
def create_event():
    data = request.get_json()
    # validation + save logic here
    return jsonify({"message": "Event created"}), 201

#TODO - Requires additional work (run redis in docker or similar) to make this endpoint work..
#@events_bp.route("/ping")
#def ping():
#    redis_client.get_client().set("status", "ok")
#    return {"status": redis_client.get_client().get("status").decode()}
