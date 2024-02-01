# Third-party imports
from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

# file imports
from fantasy_app.scores import current_week, get_most_position_points, order_positions_by_points, get_highest_points
from fantasy_app.contests import contest_list


# Initialize firebase
cred = credentials.Certificate("./CREDS.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Initialize application
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/')
def hello1():
    return jsonify('This is working')

# used for testing the retrieval of results
@app.route('/most_points_get', methods=['GET'])
def calculate_most_points_get():
    result_dict = {}
    contest = 'total_lb_points'
    points = get_most_position_points(contest_list[contest]['position'],
            current_week() - 1)
    result_dict['contest_results'] = order_positions_by_points(points)
    result_dict['contest'] = contest
    return jsonify(result_dict)

@app.route('/most_points_post', methods=['POST'])
def calculate_most_points_post():
    result_dict = {}
    point_request = request.get_json()
    contest = point_request['contest']
    week = point_request['week']
    year = point_request['year']
    
    points = get_most_position_points(
        contest_list[contest]['position'], contest_list[contest]['stat'], year, week)
    if contest_list[contest].get('single'):
        points = get_highest_points(points)

    result_dict['contest_results'] = order_positions_by_points(points)
    result_dict['contest'] = contest
    result_dict['week'] = week
    output_week = "week_" + str(week)

    # Add data to firestore
    db = firestore.client()
    doc_ref = db.collection(year).document(output_week)
    doc_ref.set(result_dict)
    return '{"status":"200", "data": "OK"}'