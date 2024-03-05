#!/usr/bin/python3
""" State Object API routes """"
from flask import Flask, Blueprint, jsonify, request, abort
from models import Place, City, User

# Assuming you have already defined your SQLAlchemy models and Flask app

# Create a Blueprint instance for the places view
places_bp = Blueprint('places', __name__, url_prefix='/api/v1')

# Define routes and actions for the places view

@places_bp.route('/cities/<city_id>/places', methods=['GET'])
def get_places_by_city(city_id):
    # Check if the city exists
    city = City.query.get(city_id)
    if not city:
        abort(404)

    # Retrieve all places in the city
    places = Place.query.filter_by(city_id=city_id).all()
    return jsonify([place.to_dict() for place in places])

@places_bp.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    # Check if the place exists
    place = Place.query.get(place_id)
    if not place:
        abort(404)

    return jsonify(place.to_dict())

@places_bp.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    # Check if the place exists
    place = Place.query.get(place_id)
    if not place:
        abort(404)

    # Delete the place
    place.delete()
    return jsonify({}), 200

@places_bp.route('/cities/<city_id>/places', methods=['POST'])
def create_place(city_id):
    # Check if the city exists
    city = City.query.get(city_id)
    if not city:
        abort(404)

    # Parse request JSON
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')

    # Check if user_id is provided
    if 'user_id' not in data:
        abort(400, 'Missing user_id')

    # Check if user exists
    user = User.query.get(data['user_id'])
    if not user:
        abort(404, 'User not found')

    # Check if name is provided
    if 'name' not in data:
        abort(400, 'Missing name')

    # Create a new place
    place = Place(name=data['name'], city_id=city_id, user_id=data['user_id'])
    place.save()

    return jsonify(place.to_dict()), 201

@places_bp.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    # Check if the place exists
    place = Place.query.get(place_id)
    if not place:
        abort(404)

    # Parse request JSON
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')

    # Update the place with the provided data
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)

    place.save()

    return jsonify(place.to_dict()), 200
