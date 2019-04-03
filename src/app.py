from flask import Flask
from flask_cors import CORS

from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.UserView import user_api as user_blueprint
# import recipepost_api blueprint
from .views.RecipepostView import recipepost_api as recipepost_blueprint

def create_app(env_name):
  """
  Create app
  """
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  CORS(app)
  # initializing bcrypt
  bcrypt.init_app(app)
  db.init_app(app)

  app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
  app.register_blueprint(recipepost_blueprint, url_prefix='/api/v1/recipeposts')

  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    return 'Congratulations! Your first endpoint is workin'

  return app