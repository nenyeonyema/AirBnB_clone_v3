#!/usr/bin/python3
""" Define a method to handle teardown app context """
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)

# Allow CORS for all domains for now
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handler for 404 errors."""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    # Run the Flask server
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
