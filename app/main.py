from flask_openapi3 import OpenAPI
from app.database import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.middlewares import middleware

from app.controllers.auth_controller import auth_bp
from app.controllers.task_controller import task_bp


jwt = {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

security_schemas = {"jwt": jwt}

app = OpenAPI(__name__)
CORS(app, origins="*", methods='*')
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["JWT_SECRET_KEY"] = "super-secret"


migrate = Migrate(app, db)
jwt = JWTManager(app)

middleware.configure_cors(app)

app.register_api(task_bp)
app.register_api(auth_bp)
