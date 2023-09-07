import os
from .espn_api_submodule.espn_api.football.league import League


# load environment variables
LEAGUE_ID = os.getenv('LEAGUE_ID')
ESPN_S2 = os.getenv('ESPN_S2')
SWID = os.getenv('SWID')

league = League(
    league_id=LEAGUE_ID,
    year=2021,
    espn_s2=ESPN_S2,
    swid=SWID
)


def hello11():
    return "Helllloooo"


def current_week():
    return league.current_week
