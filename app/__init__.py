from flask import Flask
from config import Config




def create_app():

  app = Flask(__name__)

  from app.extract import bp as extract_bp
  app.register_blueprint(extract_bp,url_prefix="/extract")


  @app.route("/testing")
  def test_route():
    return "the test route works"





  return app












