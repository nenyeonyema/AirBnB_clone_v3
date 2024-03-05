#!/usr/bin/python3
""" Creates a default RESTFUL API for the route """

from flask import jsonify, request
from api.v1.views import app_views
from models import storage, State
from uuid import uuid4


@app_views.route('/states', methods=['GET'])
def get_states():
    """ Gets state data default """
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """ Gets state data """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'Not found'}), 404
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """ Deletes state route """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'Not found'}), 404
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'])
def create_state():
    """ Creates a state storage route """
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Not a JSON'}), 400
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    state = State(name=data['name'])
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """ Updates the states dtorage """
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({'error': 'Not found'}), 404
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Not a JSON'}), 400
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
