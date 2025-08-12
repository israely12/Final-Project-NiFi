from flask import Flask
from src.rest_api.routes.funnel_routes import funnel_bp
from src.rest_api.routes.process_group_routes import process_group_bp
from src.rest_api.routes.input_port_routes import input_port_bp
from src.rest_api.routes.output_port_routes import output_port_bp
from src.rest_api.routes.connection_routes import connection_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(funnel_bp, url_prefix="/funnel")
    app.register_blueprint(process_group_bp, url_prefix="/process-group")
    app.register_blueprint(input_port_bp, url_prefix="/input-port")
    app.register_blueprint(output_port_bp, url_prefix="/output-port")
    app.register_blueprint(connection_bp, url_prefix="/connection")
    return app
