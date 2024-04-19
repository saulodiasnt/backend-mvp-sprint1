from flask import request, g
from flask_jwt_extended import decode_token
from app.models.user import User
from app.shared.erros import UnauthorizedException

EXCLUDE_ROUTES = ["/login", "/register", "/openapi"]

def configure_cors(app):
    @app.after_request
    def add_cor_headers(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        return response


def auth_check_middleware(app):
    @app.before_request
    def auth_check_middleware():
        if not any(request.path.startswith(route) for route in EXCLUDE_ROUTES):
            token = request.headers.get("Authorization")
            if not token and request.method == "OPTIONS":
                return {"message": "ok"}
            if token:
                parts = token.split()
                if len(parts) == 2:
                    token = parts[1]
                else:
                    token = parts[0]
                try:
                    decoded_token = decode_token(token)
                    user_id = decoded_token.get("sub")

                    user = User.query.filter_by(id=user_id).first()

                    if user:
                        g.current_user = user
                    else:
                        return UnauthorizedException().to_dict()
                except Exception as e:
                    return UnauthorizedException().to_dict()

            else:
                return UnauthorizedException().to_dict()