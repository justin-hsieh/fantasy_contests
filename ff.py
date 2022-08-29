from espn_api_submodule.espn_api.football import League

league = League(league_id=69192084, year=2022, espn_s2='AECtBC8t2p%2F1HWtD9xwcZTJbKZnmIy2jPmG6JJMKDE7WjJ0YmGBLZG7i%2FOkb5aGb%2F%2BpKL%2Bxe33dXnl%2F6MDJwDbrD2thKx0SwXDB2wRJF%2F0oompDwq04%2BoR9qoX0777%2Bksnn2Hr55WelNUxLArj4Ea2XCCDCTO4S%2BgW147eUAqFSf28q93COtLYtnFk1uxKRkm2awp2ZxVycaBI2TMGeC1UNYUoP2wJBw%2F9s%2F2BPJKUC6hz8NtlXO2lSauKcY4cGxfSHfrfnOf0kgfJIJephWMeXYox9Hb7e7MRmd1TwLuL%2FP2w%3D%3D',swid='{832BF702-905D-40ED-ABF7-02905D90EDB1}')


team = league.teams

#player = team.roster[0]
#print(team[0].team_id, team[0].team_abbrev, team[0].team_name)
#print(team[0].roster)
#print(player.stats)
#box_scores = league.box_scores(12)[0].home_lineup[4].stats[12]

box_score = league.box_scores()
#print(box_scores)
#print(league.box_scores(12)[0].home_lineup)
#print(box_scores[0].home_team.roster[0].stats)
#box_score[0].away_lineup
#id = league.teams[0].roster[0].playerId
#print(league.player_info(playerId=id))
'''
for i in team:
    print(i)
    print(i.final_standing)
'''
#box_scores = league.box_scores(12)[0].home_lineup[0].game_played
#print(box_score)
#print(league.box_scores(12)[0].home_lineup[4])
'''
for i in range(len(box_score)):
    matchup = box_score[i]
    for j in range(len(matchup.home_lineup)):
        print(matchup.home_lineup)
'''

def get_most_position_points(matchups, position):
    for matchup in range(len(matchups)):
        away = box_score[matchup].away_lineup
        home = box_score[matchup].home_lineup
        for player in range(len(away)):
            if away[player].slot_position == position:
                print(player)
                print(away[player].name)
                print(away[player].points)

get_most_position_points(box_score, 'RB')