from flask_sqlalchemy import SQLAlchemy

from app.modules.shared.base_class import Base

db = SQLAlchemy(model_class=Base)
