import requests
import json

URL_CARDS = "https://api.clashroyale.com/v1/cards"
URL_TOURNAMENTS = "https://api.clashroyale.com/v1/tournaments"
URL_PLAYERS = "https://api.clashroyale.com/v1/players"

headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjM5N2NlZjM5LWRiMzktNGVmZS04YzJiLTZiZjQ4YTQ2MTYwYyIsImlhdCI6MTcyNzgzNjk5Niwic3ViIjoiZGV2ZWxvcGVyLzdjYWZiOGFhLTA5ZjktNzdmOC0wZTBiLTAzYmQ3YThlZGFkOCIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMTAuMTQ0Ljk1Il0sInR5cGUiOiJjbGllbnQifV19.jiHlhqS2vfl92bprsI0GQ0nd9oaR7kH_49EE2mH7N_fIKOwWXANpG7DNiGUU4kOTRbos1sBHdKkfSdRupRix0Q"
}

def get_all_cards():
    response = requests.get(url=URL_CARDS, headers=headers)
    if response.status_code == 200:
        items_obj = json.loads(response.text)
        items_list = items_obj.get('items')

        for item in items_list:
            print('Id:', str(item['id']))
            print('Nome:', item['name'])
            print('Max Level:', str(item['maxLevel']))
            print('Imagem:', item['iconUrls']['medium'])
            print('======================================')

def get_all_tournaments():
    response = requests.get(url=URL_TOURNAMENTS + "?name=a", headers=headers)
    if response.status_code == 200:
        items_obj = json.loads(response.text)
        items_list = items_obj.get('items')
        for item in items_list:
            print('Tag:', str(item['tag']))
            print('Nome:', item['name'])
            print('Status:', item['status'])
            print('Duracao:', str(item['duration']))
            print('======================================')

def get_all_players():
    response = requests.get(url=URL_PLAYERS + "?name=a", headers=headers)
    if response.status_code == 200:
        items_obj = json.loads(response.text)
        items_list = items_obj.get('items')
        for item in items_list:
            print('Nickname:', item['name'])
            print('Tempo de Jogo:', item['playTime'])
            print('Troféus:', item['trophies'])
            print('Nível:', item['level'])
            print('======================================')

def get_all_battles():
    print("======================================")

def get_all_decks():
    print("======================================")

def get_all_player_statistics():
    print("======================================")


def get_all_trophy_history():
    print("======================================")

get_all_cards()
get_all_tournaments()
get_all_players()
get_all_battles()
get_all_decks()
get_all_player_statistics()
get_all_trophy_history()
