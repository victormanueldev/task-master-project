from app.dependecy_container import create_context

context, app = create_context()

from app.extensions.bcrypt import bcrypt
from app.extensions.db import db
from app.extensions.jwt import jwt
from app.modules.auth.views import auth
from app.modules.shared.error_class import ErrorBase, error_handler
from app.modules.users.views import users

# Initialize extensions:
db.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)

# Register blueprints:
app.register_blueprint(auth, url_prefix="/api/v1/auth")
app.register_blueprint(users, url_prefix="/api/v1/users")
app.register_error_handler(ErrorBase, error_handler)

if __name__ == "__main__":
    app.run()
