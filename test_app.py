from app import app
import json

def test_hello1_route():
    response = app.test_client().get('/')
    json_response = response.get_json()
    assert json_response == 'This is working'
    assert response.status_code == 200
    
def test_calculate_most_points_get():
    response = app.test_client().get('/most_points_get')
    json_response = response.get_json()
    assert list(json_response.keys()) == ['contest', 'contest_results']
    assert response.status_code == 200

def test_calculate_most_points_post():
    response = app.test_client().post('/most_points_post', 
                                      json={
                                          "contest": "total_lb_tackles",
                                          "week": 14,
                                          "year": "2023"})
    json_response = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert json_response == {'status':'200', 'data': 'OK'}

    response = app.test_client().post('/most_points_post', 
                                      json={
                                          "contest": "highest_single_starter_points",
                                          "week": 8,
                                          "year": "2022"})
    json_response = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert json_response == {'status':'200', 'data': 'OK'}