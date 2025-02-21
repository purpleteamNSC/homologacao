import os
import requests
from dotenv import load_dotenv

load_dotenv()

helix_id = os.getenv('helix_id')
api_key = os.getenv('api_key')

def get_alerts():
    url=f'https://apps.fireeye.com/helix/id/{helix_id}/api/v3/alerts/'
    headers = {
        "accept":"application/json",
        "x-fireeye-api-key": api_key
    }

    res = requests.get(url,headers=headers)

    res.raise_for_status()

    data = res.json()
    results = data['results']

    return results

    print(data.items)

results = get_alerts()

for result in results:
    print(result['message'])