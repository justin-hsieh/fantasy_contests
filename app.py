# Third-party imports
from flask import Flask, jsonify, request
import json
# from decouple import config
from fantasy_app.functions import current_week, get_most_position_points, order_positions_by_points
from fantasy_app.contest_list import contests


# app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app = Flask(__name__)

# stop tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB.init_app(app)


@app.route('/')
def hello1():
    return jsonify('This is working')


@app.route('/test_submodule', methods=['GET'])
def submodule():
    week = current_week()
    return jsonify(str(week))


'''
@app.route('/get_teams', methods=['GET'])
def get_team():
    teams = list(get_team_list())
    print(teams)
    return jsonify(teams)



@app.route('/test', methods=['GET','POST'])
def highest_score():

    pos = request.get_json()
    position = pos['contest']
    points = get_most_position_points(contests[position]['position_list'])
    points1 = highest_single_player(points)
    #rank = order_positions_by_points(points)
    data = json.dumps(points1)
    return data
'''


@app.route('/most_points_get', methods=['GET'])
def calculate_most_points_get():
    stat = 'total_de_points'
    points = get_most_position_points(
        contests[stat]['position_list'], current_week())
    ranks = order_positions_by_points(points)
    data = json.dumps(ranks)
    return jsonify(data)


@app.route('/most_points_post', methods=['POST'])
def calculate_most_points_post():
    point_request = request.get_json()
    stat = point_request['contest']
    points = get_most_position_points(
        contests[stat]['position_list'], current_week())
    ranks = order_positions_by_points(points)
    data = json.dumps(ranks)
    return jsonify(data)
