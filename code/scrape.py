#! /usr/bin/env python3

import requests
import json
from pathlib import Path
from datetime import datetime

COOKIE_PATH = 'cookies.json'
COOKIES = json.loads(Path(COOKIE_PATH).read_text())

def main():
    url = 'https://api.ageofempires.com/api/v1/mods/FindAsUser'
    response = requests.post(url, json={'start': 1, 'count': 1000, 'q': "", 'game': 2, 'modid': 0, 'filter': 15, 'status': "", 'sort': "createDate", 'order': "DESC"}, cookies=COOKIES)
    all_the_maps = response.json()
    
    download_urls = {}
    for map_ in all_the_maps['modList']:
        try:
            mod_id = map_['modId']
            mod_url = 'https://api.ageofempires.com/api/v1/mods/Install'
            mod_response = requests.post(mod_url, json={'modid': str(mod_id)}, cookies=COOKIES)
            if mod_response.status_code != 200:
                print(f'Received non-200 response: {mod_response.status_code}')
                print(mod_response.text)
            mod_details = mod_response.json()
            map_['downloadUrl'] = mod_details['value']['downloadUrl']
        except:
            print(f'Could not fetch details for mod {mod_id}')
    all_the_maps['lastUpdate'] = datetime.utcnow().strftime('%Y-%m-%d')
    Path('all_the_maps.json').write_text(json.dumps(all_the_maps, indent=4))


if __name__ == '__main__':
    main()
