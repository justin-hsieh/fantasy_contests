# Third-party imports
from flask import Flask
from decouple import config


def create_app():

    app = Flask(__name__, instance_relative_config=True)
    #app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # stop tracking modifications
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #DB.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello, World!!'


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!!'
    
    return app