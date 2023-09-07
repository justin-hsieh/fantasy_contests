# Third-party imports
from flask import Flask, jsonify, request
import json
# from decouple import config
from fantasy_app.functions import hello11
from fantasy_app.contest_list import contests


# app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app = Flask(__name__)

# stop tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB.init_app(app)


@app.route('/')
def hello1():
    return 'Hello, World!!'


'''
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
    

    @app.route('/test_submodule', methods=['GET'])
    def submodule():
        week = current_week()
        return str(week)
        
    @app.route('/most_points', methods=['GET', 'POST'])
    def calculate_yards():
        position =  'total_punter_points'
        points = get_most_position_points(contests[position]['position_list'], 8)
        ranks = order_positions_by_points(points)
        data = json.dumps(ranks)
        return jsonify(data)
    '''
