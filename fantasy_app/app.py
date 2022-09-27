# Third-party imports
from flask import Flask, jsonify, request
import json

#import requests
#import espn_api_submodule
#from decouple import config
from .testing import test_endpoint
from .ff import get_most_position_points, highest_single_player, order_positions_by_points, get_yards
from .lists import contests
def create_app():
        #app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
        app = Flask(__name__)

        # stop tracking modifications
        #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        #DB.init_app(app)
        @app.route('/')
        def hello1():
            return 'Hello, World!!'

        @app.route('/test', methods=['GET','POST'])
        def highest_score():
     
            pos = request.get_json()
            position = pos['contest']
            points = get_most_position_points(contests[position]['position_list'])
            points1 = highest_single_player(points)
            #rank = order_positions_by_points(points)
            data = json.dumps(points1)
            return data

        @app.route('/point', methods=['GET','POST'])
        def testings():
            j = request.get_json()
            position = j['position']
            response = get_yards(position)
            data = json.dumps(response)

            return data
        return app



'''
if __name__ == "__main__":
    app.run(debug=True)
'''