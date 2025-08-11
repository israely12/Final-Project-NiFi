from flask import Flask
from src.rest_api.routes.funnel_routes import funnel_bp
from src.rest_api.routes.process_group_routes import process_group_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(funnel_bp, url_prefix="/funnel")
    app.register_blueprint(process_group_bp, url_prefix="/process-group")
    return app
