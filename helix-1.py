import os
import requests
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

helix_id = os.getenv("helix_id")
api_key = os.getenv("api_key")


def get_alerts():
    url = f"https://apps.fireeye.com/helix/id/{helix_id}/api/v3/alerts/"
    headers = {"accept": "application/json", "x-fireeye-api-key": api_key}
    params = {
        "limit":"100",
        "state":"Closed"
    }

    res = requests.get(url, headers=headers, params=params)

    

    res.raise_for_status()

    data = res.json()
    # meta = data['meta']
    results = data['results']

    return results


results = get_alerts()
count=1
for result in results:
    # if (result['message'] == 'TEST ALERT [Helix]') or (result['message'] == 'RULE01'):
    #     continue
    print(f" {count} - {result['message']}")
    count = count+1





   """
   DEMANDA:
   - fechar todos os casos que estao abertos no helix

   REQUISITOS:
   - filtrar os casos abertos
   - buscar os casos
   - enviar comando para fechar
   """
