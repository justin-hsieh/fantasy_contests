# Third-party imports
from flask import Flask, jsonify, request
import json
from flask_cors import CORS
# from decouple import config
from fantasy_app.functions import get_current_matchups, current_week, get_most_position_points, order_positions_by_points
from fantasy_app.contest_list import contests
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./CREDS.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


# app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
app = Flask(__name__)
CORS(app, supports_credentials=True)
# stop tracking modifications
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DB.init_app(app)


@app.route('/')
def hello1():
    return jsonify('This is working')


@app.route('/test_submodule', methods=['GET'])
def submodule():
    matchups = get_current_matchups()

    return jsonify(str(matchups))


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
    contest_dict = {}
    stat = 'total_lb_points'
    points = get_most_position_points(
        contests[stat]['position_list'], current_week()-1)
    contest_dict['contest_results'] = order_positions_by_points(points)
    contest_dict['contest'] = stat

    return jsonify(contest_dict)


@app.route('/most_points_post', methods=['POST'])
def calculate_most_points_post():
    contest_dict = {}
    point_request = request.get_json()
    stat = point_request['contest']
    week = int(point_request['week'])
    year = point_request['year']
    points = get_most_position_points(
        contests[stat]['position_list'], week)
    contest_dict['contest_results'] = order_positions_by_points(points)
    contest_dict['contest'] = stat
    contest_dict['week'] = week
    output_week = "week_" + str(week)
    db = firestore.client()
    doc_ref = db.collection(year).document(output_week)
    doc_ref.set(contest_dict)
    return '{"status":"200", "data": "OK"}'
