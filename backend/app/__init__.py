from flask import Flask, jsonify

from .config import Config
from .extensions import db
from .routes.auth_routes import auth_bp
from .routes.dashboard_routes import dashboard_bp
from .routes.project_routes import project_bp
from .routes.report_routes import report_bp
from .routes.org_routes import org_bp
from .routes.pin_routes import pin_bp
from .routes.user_routes import user_bp
from .routes.audit_routes import audit_bp


def create_app(config_class: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    register_blueprints(app)

    @app.get("/api/health")
    def health_check():
        return jsonify(status="ok"), 200

    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")
    app.register_blueprint(project_bp, url_prefix="/api/projects")
    app.register_blueprint(report_bp, url_prefix="/api/projects")
    app.register_blueprint(org_bp, url_prefix="/api/orgs")
    app.register_blueprint(pin_bp, url_prefix="/api/orgs")
    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(audit_bp, url_prefix="/api/audit-logs")

