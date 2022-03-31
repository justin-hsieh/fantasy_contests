from espn_api_submodule.espn_api.football import League

league = League(league_id=69192084, year=2021, espn_s2='AECtBC8t2p%2F1HWtD9xwcZTJbKZnmIy2jPmG6JJMKDE7WjJ0YmGBLZG7i%2FOkb5aGb%2F%2BpKL%2Bxe33dXnl%2F6MDJwDbrD2thKx0SwXDB2wRJF%2F0oompDwq04%2BoR9qoX0777%2Bksnn2Hr55WelNUxLArj4Ea2XCCDCTO4S%2BgW147eUAqFSf28q93COtLYtnFk1uxKRkm2awp2ZxVycaBI2TMGeC1UNYUoP2wJBw%2F9s%2F2BPJKUC6hz8NtlXO2lSauKcY4cGxfSHfrfnOf0kgfJIJephWMeXYox9Hb7e7MRmd1TwLuL%2FP2w%3D%3D', swid='{832BF702-905D-40ED-ABF7-02905D90EDB1}')


team = league.teams[0]

player = team.roster[0]


box_scores = league.box_scores(12)
print(box_scores[0].home_lineup)
print(box_scores[0].home_lineup[11].slot_position)