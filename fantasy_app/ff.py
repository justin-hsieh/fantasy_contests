#import sys
#sys.path.append('..')
from espn_api_submodule.espn_api.football import League
#from lists import contests

league = League(
    league_id=69192084,
    year=2022,
    espn_s2='AECtBC8t2p%2F1HWtD9xwcZTJbKZnmIy2jPmG6JJMKDE7WjJ0YmGBLZG7i%2FOkb5aGb%2F%2BpKL%2Bxe33dXnl%2F6MDJwDbrD2thKx0SwXDB2wRJF%2F0oompDwq04%2BoR9qoX0777%2Bksnn2Hr55WelNUxLArj4Ea2XCCDCTO4S%2BgW147eUAqFSf28q93COtLYtnFk1uxKRkm2awp2ZxVycaBI2TMGeC1UNYUoP2wJBw%2F9s%2F2BPJKUC6hz8NtlXO2lSauKcY4cGxfSHfrfnOf0kgfJIJephWMeXYox9Hb7e7MRmd1TwLuL%2FP2w%3D%3D',
    swid='{832BF702-905D-40ED-ABF7-02905D90EDB1}'
    )


currentweek = league.current_week
#print(league.teams)
box_scores = league.box_scores()[0].home_lineup[17].stats

box_score = league.box_scores(12)

box_score1 = league.box_scores(1)[2].home_lineup[8].game_played
#print(league.box_scores(1)[2].home_lineup[21].stats)
#print(box_score1)
#matchups = league.box_scores(week)
#position = ['RB']
'''
for index, matchup in enumerate(matchups):
        away = matchup.away_lineup
        home = matchup.home_lineup
        for player, value in enumerate(home):
            if value.slot_position in position:
                #print(player, value)
'''
def get_matchups(current_week):
    matchups = league.box_scores(currentweek)
    return matchups

def get_lineups(matchups):
    for matchup_index, matchup in enumerate(matchups):
        away = matchup.away_lineup
        home = matchup.home_lineup
    return home, away
matchups = get_matchups(currentweek)
#print(get_lineups(matchups))


def get_yards(position, stat, currentweek):
    matchups = league.box_scores(currentweek)
    player_dict = {}
    for matchup_index, matchup in enumerate(matchups):
        away = matchup.away_lineup
        home = matchup.home_lineup
    
        for player_index, player in enumerate(away):
            if player.slot_position in position:
                team = matchup.away_team.team_name
                if team in player_dict:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team]['player'].update({(player.name): player.stats[currentweek]['breakdown'][stat]})
                        else:
                            player_dict[team]['player'].update({(player.name): 0})
                    else:
                        player_dict[team]['player'].update({(player.name): 0})
                else:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team] = {'player': {(player.name): player.stats[currentweek]['breakdown'][stat]}}
                        else:
                            player_dict[team] = {'player': {(player.name): 0}}
                    else:
                        player_dict[team] = {'player': {(player.name): 0}}
        for player_index, player in enumerate(home):
            if player.slot_position in position:
                team = matchup.home_team.team_name
                if team in player_dict:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team]['player'].update({(player.name): player.stats[currentweek]['breakdown'][stat]})
                        else:
                            player_dict[team]['player'].update({(player.name): 0})
                    else:
                        player_dict[team]['player'].update({(player.name): 0})
                else:
                    if player.stats[currentweek].get('breakdown'):
                        if player.stats[currentweek]['breakdown'].get(stat):
                            player_dict[team] = {'player': {(player.name): player.stats[currentweek]['breakdown'][stat]}}
                        else:
                            player_dict[team] = {'player': {(player.name): 0}}
                    else:
                        player_dict[team] = {'player': {(player.name): 0}}
    
    return player_dict
dict1 = get_yards(['P'], '139', 1)
#print(dict1)

def get_most_position_points(position):
    matchups = league.box_scores()
    player_dict = {}
    for matchup in range(len(matchups)):
        away = box_score[matchup].away_lineup
        home = box_score[matchup].home_lineup
        for player in range(len(away)):
            if away[player].slot_position in position:
                if box_score[matchup].away_team.team_name in player_dict:
                    player_dict[box_score[matchup].away_team.team_name]['player'].update({(away[player].name): away[player].points})
                else:
                    player_dict[box_score[matchup].away_team.team_name] = {'player': {(away[player].name): away[player].points}}
        for player in range(len(home)):
            if home[player].slot_position in position:
                if box_score[matchup].home_team.team_name in player_dict:
                    player_dict[box_score[matchup].home_team.team_name]['player'].update({(home[player].name): home[player].points})
                else:
                    player_dict[box_score[matchup].home_team.team_name] = {'player': {(home[player].name): home[player].points}}

    return player_dict
    
def order_positions_by_points(player_dict):

    for team, info in player_dict.items():
        player_dict[team].update({'total' : round(sum(info['player'].values()), 2)})
    result = dict(sorted(player_dict.items(), key=lambda x: x[1]['total'], reverse=True))

    return result

def highest_single_player(player_dict):
    final_dict = {}
    for team, info in player_dict.items():
        final_dict[team] = {'player' : max(info['player'], key=info['player'].get)}
        final_dict[team].update({'total': max(info['player'].values())})
    result = dict(sorted(final_dict.items(), key= lambda x: x[1]['total'], reverse=True))
    return result

dict1 = get_most_position_points(['TE'])
#dict2 = highest_single_player(dict1)

#print(dict1)
#print(order_positions_by_points(dict1))
