import os
import json
import operator
from datetime import datetime
from dotenv import load_dotenv
from .espn_api_submodule.espn_api.football.league import League


# load environment variables
load_dotenv()
LEAGUE_ID = os.getenv('LEAGUE_ID')
ESPN_S2 = os.getenv('ESPN_S2')
SWID = os.getenv('SWID')


# retrieve football year
def get_year():
    currentMonth = datetime.now().month
    if currentMonth > 7:
        currentYear = datetime.now().year
    else:
        currentYear = datetime.now().year - 1
    return currentYear


def current_week():
    return league.current_week


def get_week():
    today = datetime.date.today()
    weekday_number = today.weekday()
    week = current_week()

    if weekday_number < 3:
        week = current_week() - 1
    return week


league = League(
    league_id=LEAGUE_ID,
    year=get_year(),
    espn_s2=ESPN_S2,
    swid=SWID
)


def get_team_list():
    return league.teams


def get_current_matchups():
    matchups = league.box_scores(current_week())
    return matchups


def get_highest(position, stat, currentweek=0):
    if currentweek > 0:
        matchups = league.box_scores(currentweek)
    else:
        matchups = get_current_matchups()
        currentweek = get_week()
    player_dict = {}
    for matchup_index, matchup in enumerate(matchups):
        away = matchup.away_lineup
        home = matchup.home_lineup
        create_dictionary(away)
        create_dictionary(home)
    return player_dict


def create_dictionary(team_name, lineup, position, stat, player_dict):

    currentweek = get_week()
    for player_index, player in enumerate(lineup):
        if player.slot_position in position:
            if team_name in player_dict:
                if player.stats[currentweek].get('breakdown'):
                    if player.stats[currentweek]['breakdown'].get(stat):
                        player_dict[team_name]['player'].update(
                            {(player.name): player.stats[currentweek]['breakdown'][stat]})
                    else:
                        player_dict[team_name]['player'].update(
                            {(player.name): 0})
                else:
                    player_dict[team_name]['player'].update({(player.name): 0})
            else:
                if player.stats[currentweek].get('breakdown'):
                    if player.stats[currentweek]['breakdown'].get(stat):
                        player_dict[team_name] = {'player': {
                            (player.name): player.stats[currentweek]['breakdown'][stat]}}
                    else:
                        player_dict[team_name] = {'player': {(player.name): 0}}
                else:
                    player_dict[team_name] = {'player': {(player.name): 0}}
        return
    '''
    for player_index, player in enumerate(home):
        if player.slot_position in position:
            team = matchup.home_team.team_name
            if team in player_dict:
                if player.stats[currentweek].get('breakdown'):
                    if player.stats[currentweek]['breakdown'].get(stat):
                        player_dict[team]['player'].update(
                            {(player.name): player.stats[currentweek]['breakdown'][stat]})
                    else:
                        player_dict[team]['player'].update(
                            {(player.name): 0})
                else:
                    player_dict[team]['player'].update({(player.name): 0})
            else:
                if player.stats[currentweek].get('breakdown'):
                    if player.stats[currentweek]['breakdown'].get(stat):
                        player_dict[team] = {'player': {
                            (player.name): player.stats[currentweek]['breakdown'][stat]}}
                    else:
                        player_dict[team] = {'player': {(player.name): 0}}
                else:
                    player_dict[team] = {'player': {(player.name): 0}}
    '''
    return player_dict


# print(get_highest(['WR'], 'receivingReceptions', current_week()))
def new_dict(position, current_dict, lineup):
    count = 0
    total_score = 0
    for player in lineup:
        if player.slot_position in position:
            count += 1
            current_dict['player{}'.format(count)] = {
                'name': player.name,
                'score': player.points,
                'game_played': player.game_played
            }
            total_score += player.points
    current_dict['total_score'] = total_score
    return current_dict


def get_most_position_points(position, currentweek=0):
    if currentweek > 0:
        matchups = league.box_scores(currentweek)
    else:
        matchups = get_current_matchups()
        currentweek = current_week()
    matchups_list = []

    for matchup in matchups:
        player_dict = {}
        player_dict1 = {}
        away = matchup.away_lineup
        home = matchup.home_lineup

        player_dict['team'] = matchup.away_team.team_name
        player_dict1['team'] = matchup.home_team.team_name

        away_dict = new_dict(
            position, player_dict, away)
        home_dict = new_dict(
            position, player_dict1, home)
        matchups_list.append(away_dict)
        matchups_list.append(home_dict)
    return matchups_list


dict1 = get_most_position_points(['WR'], 1)


def order_positions_by_points(score_list):
    sorted_list = sorted(score_list, key=operator.itemgetter(
        'total_score'), reverse=True)
    return sorted_list


# print(order_positions_by_points(dict1))
