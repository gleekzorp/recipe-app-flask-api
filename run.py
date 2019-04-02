# Use this for local testing
# Don't forget to setup local environment configs
import os

from src.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  app = create_app(env_name)
  # run app
  app.run()



# Use this for Heroku Deploy
# import os
# from src.app import create_app

# env_name = os.getenv('FLASK_ENV')
# app = create_app(env_name)

# if __name__ == '__main__':
#   port = os.getenv('PORT')
#   # run app
#   app.run(host='0.0.0.0', port=port)