import requests
import json
from db import Soccer

league_id_1 = '**************************link******************************'
league_id_2 = '**************************link******************************'
league_id_3 = '**************************link******************************'
league_id_4 = '**************************link******************************'

links = [league_id_1, league_id_2, league_id_3, league_id_4]

def Extract_data(api_uri):

    all_data = {'data':[]} #Enpty dict to group all data requested from APIs in one data structure.

    for url in api_uri:

        response = requests.get(url, verify=False)
        
        data = response.text
        
        parsed_data = json.loads(data) # return a dict  
        
        # append filtred data to the all_data dict 

        for items in parsed_data['data']:
            if items['season'] != "Season 2020/2021":
                pass
            elif items['competition'] == "Sky Bet Championship" and items['season'] == "Season 2020/2021" and isinstance(items['round'], int) == False:
                pass
            else:
                all_data['data'].append(items)  

    return all_data

soccer_data = Extract_data(links)


# INSTANTIATE THE SOCCER CLASS
 
the_database = Soccer()

# LOAD DATA TO VENUE TABLE
def load_match_data():

    #columns = [id, feedMatchId, skyId, competition,competitionId, status, period, seasonId, round, type, minute, date]
    match_record = [
        (data['id'],data['feedMatchId'],data['skyId'],data['competition'],data['competitionId'],data['status'],
    data['period'],data['round'],data['type'],data['minute'],data['lastUpdated'],data['date'],data['seasonId'],
    data['venue']['id'] ,data['homeTeam']['id'], data['homeTeam']['skyId'], data['homeTeam']['name'], 
    data['homeTeam']['shortName'], data['homeTeam']['abbreviation'], data['homeTeam']['score'], data['homeTeam']['halfTimeScore'],
    data['awayTeam']['id'], data['awayTeam']['skyId'], data['awayTeam']['name'], data['awayTeam']['shortName'], 
    data['awayTeam']['abbreviation'], data['awayTeam']['score'], data['awayTeam']['halfTimeScore'])
    for data in soccer_data['data']
    ]
    the_database.insert_into_match(match_record)

def load_venue_data():
    #columns =  [venueid, name, location]
    venue_items = [(data['venue']['id'], data['venue']['name'],data['venue']['location']) for data in soccer_data['data']]
    #print(venue_items)
    the_database.insert_into_venue(venue_items)

# LOAD DATA TO SEASON TABLE

def load_season_data():
    #columns = [seasonid, season]
    season_items = [(data['seasonId'],data['season']) for data in soccer_data['data']]
    the_database.insert_into_season(season_items)


if __name__ == "__main__":

    load_season_data()
    load_venue_data()
    load_match_data()
