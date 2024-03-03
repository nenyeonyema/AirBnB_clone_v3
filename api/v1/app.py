#!/usr/bin/python3
""" Define a method to handle teardown app context """
from flask import Flask
from api.v1.views import app_views
from models import storage
import os

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Closes the storage connection"""
    storage.close()


if __name__ == '__main__':
    # Run the Flask server
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
