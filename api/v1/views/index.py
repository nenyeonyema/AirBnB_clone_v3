#!/usr/bin/python3
"""
create a route /status on the object
app_views that returns a JSON: "status": "OK"
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/api/v1/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """Retrieve the number of each object by type"""
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
