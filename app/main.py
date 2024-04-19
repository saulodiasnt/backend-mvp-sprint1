from flask_openapi3 import OpenAPI
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

jwt = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

security_schemas = {"jwt": jwt}

app = OpenAPI(__name__)
CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["JWT_SECRET_KEY"] = "super-secret"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# flake8: noqa F401
from app.models import user

# flake8: noqa F401
from app.models import task

# flake8: noqa F401
from app.middlewares.auth_check_middleware import auth_check_middleware

from app.controllers.auth_controller import auth_bp
from app.controllers.task_controller import task_bp

app.register_api(task_bp)
app.register_api(auth_bp)
