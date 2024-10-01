from flask import Blueprint

bp = Blueprint("extract",__name__)

from app.extract import routes