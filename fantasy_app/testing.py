import requests
import json
import pandas as pd
import numpy as np


def test_endpoint():
    endpoint = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/2022/segments/0/leagues/69192084'
    params = {
            'view': ['mTeam', 'mMatchup']
        }
    espn_s2='AECtBC8t2p%2F1HWtD9xwcZTJbKZnmIy2jPmG6JJMKDE7WjJ0YmGBLZG7i%2FOkb5aGb%2F%2BpKL%2Bxe33dXnl%2F6MDJwDbrD2thKx0SwXDB2wRJF%2F0oompDwq04%2BoR9qoX0777%2Bksnn2Hr55WelNUxLArj4Ea2XCCDCTO4S%2BgW147eUAqFSf28q93COtLYtnFk1uxKRkm2awp2ZxVycaBI2TMGeC1UNYUoP2wJBw%2F9s%2F2BPJKUC6hz8NtlXO2lSauKcY4cGxfSHfrfnOf0kgfJIJephWMeXYox9Hb7e7MRmd1TwLuL%2FP2w%3D%3D'
    swid='{832BF702-905D-40ED-ABF7-02905D90EDB1}'

    r = requests.get(url=endpoint, params=params, headers=None, cookies={
                'espn_s2': espn_s2,
                'SWID': swid
            })

    df = pd.json_normalize(r.json())
    
    return r.json()
