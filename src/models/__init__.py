from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
# hash passwords
bcrypt = Bcrypt()

from .RecipepostModel import RecipepostModel, RecipepostSchema
from .UserModel import UserModel, UserSchema