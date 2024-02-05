import os
import json
import operator
from datetime import datetime
from dotenv import load_dotenv
from .espn_api_submodule.espn_api.football.league import League


# load environment variables
load_dotenv()
LEAGUE_ID = os.getenv('LEAGU2')
SWID = os.getenv('SWID')
LEAGUE_ID = os.getenv('LEAGUE_ID')
ESPN_S2 = os.getenv('ESPN_S2')

with open('../OWNERS.json') as f:
    OWNERS = json.load(f)
    
# retrieve football year
def get_year():
    currentMonth = datetime.now().month
    if currentMonth > 7:
        currentYear = datetime.now().year
    else:
        currentYear = datetime.now().year - 1
    return currentYear

def league_instance(input_year):
    return League(league_id=LEAGUE_ID,year=input_year,espn_s2=ESPN_S2,swid=SWID)   

def current_week():
    league = league_instance(get_year())
    return league.current_week

def get_week():
    today = datetime.date.today()
    weekday_number = today.weekday()
    week = current_week()

    if weekday_number < 3:
        week = current_week() - 1
    return week

def get_team_list():
    league = league_instance(get_year())
    return league.teams

def get_current_matchups():
    league = league_instance(get_year())
    matchups = league.box_scores(current_week())
    return matchups

def new_dict(position, current_dict, lineup, stat, week):
    total = 0
    player_list = []
    for player in lineup:
        if player.slot_position in position:
            temp_dict = {
                    'name': player.name,
                    'game_played': player.game_played
            }
            if stat[0] != '':
                for i in stat:
                    if player.stats[week].get('breakdown'):
                        if player.stats[week]['breakdown'].get(i):
                            temp_dict['score'] = player.stats[week]['breakdown'][i]
                            total += player.stats[week]['breakdown'][i]
                        else:
                            temp_dict['score'] = 0
            else:
                temp_dict['score'] = player.points
                total += player.points
                
            player_list.append(temp_dict)
            current_dict['total_score'] = total
            current_dict['players'] = player_list
    return current_dict

def get_most_position_points(position, stat, year, currentweek=0):
    league = league_instance(int(year))
    matchups = league.box_scores(currentweek)

    matchups_list = []

    for matchup in matchups:
        player_dict = {}
        player_dict1 = {}
        away = matchup.away_lineup
        home = matchup.home_lineup

        player_dict['team_name'] = matchup.away_team.team_name
        player_dict1['team_name'] = matchup.home_team.team_name
        player_dict['team_owner'] = OWNERS[matchup.away_team.owners[0]]
        player_dict1['team_owner'] = OWNERS[matchup.home_team.owners[0]]
        
        away_dict = new_dict(
            position, player_dict, away, stat, currentweek)
        home_dict = new_dict(
            position, player_dict1, home, stat, currentweek)
        matchups_list.append(away_dict)
        matchups_list.append(home_dict)
    return matchups_list

def get_highest_points(points_dict):
    for entry in points_dict:
        entry['players'] = [max(entry['players'], key=(lambda x: x['score']))]
        entry['total_score'] = entry['players'][0]['score']
    return points_dict

def order_positions_by_points(score_list):
    sorted_list = sorted(score_list, key=operator.itemgetter(
        'total_score'), reverse=True)

    for i, member_dict in enumerate(sorted_list):
        member_dict["rank"] = i + 1
    return sorted_list

