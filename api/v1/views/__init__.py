#!/usr/bin/python3
"""
create a variable app_views
which is an instance of Blueprint
"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *

from api.v1.views import amenities

from api.v1.views import cities

from api.v1.views import places

from api.v1.views import places_reviews

from api.v1.views import states

from api.v1.views import users
