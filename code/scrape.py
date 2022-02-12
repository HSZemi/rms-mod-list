#! /usr/bin/env python3

import requests
import json
from pathlib import Path
from datetime import datetime

COOKIE_PATH = 'cookies.json'
COOKIES = json.loads(Path(COOKIE_PATH).read_text())

url = 'https://api.ageofempires.com/api/v1/mods/FindAsUser'
mod_url = 'https://api.ageofempires.com/api/v1/mods/Install'

def main():
    json_path = Path('all_the_maps.json')
    old_data = {'modList':[]}
    if json_path.is_file():
        old_data = json.loads(json_path.read_text())
    response = requests.post(url, json={'start': 1, 'count': 1000, 'q': "", 'game': 2, 'modid': 0, 'filter': 15, 'status': "", 'sort': "createDate", 'order': "DESC"}, cookies=COOKIES)
    all_the_maps = response.json()
    
    for map_ in all_the_maps['modList']:
        try:
            mod_id = map_['modId']
            cached = False
            for old_mod in old_data['modList']:
                if old_mod['modId'] == mod_id:
                    if old_mod['lastUpdate'] == map_['lastUpdate'] and old_mod['downloadUrl'].startswith('https://'):
                        cached = True
                        map_['downloadUrl'] = old_mod['downloadUrl']
                        print(f'Using cached downloadUrl for modId {mod_id}')
                    break
            if not cached:
                print(f'Fetching new downloadUrl for modId {mod_id}')
                mod_response = requests.post(mod_url, json={'modid': str(mod_id)}, cookies=COOKIES)
                if mod_response.status_code != 200:
                    print(f'Received non-200 response: {mod_response.status_code}')
                    print(mod_response.text)
                    map_['downloadUrl'] = '#'
                else:
                    mod_details = mod_response.json()
                    Path(f'{mod_id}.json').write_text(mod_response.text)
                    map_['downloadUrl'] = mod_details['value']['downloadUrl']
        except:
            print(f'Could not fetch details for mod {mod_id}')
    all_the_maps['lastUpdate'] = datetime.utcnow().strftime('%Y-%m-%d')
    json_path.write_text(json.dumps(all_the_maps, indent=4))


if __name__ == '__main__':
    main()
