import os
from pprint import pprint

import requests


meraki_key = os.environ["MERAKI_API_KEY"]
base_url = 'https://api.meraki.com/api/v0'


def get_meraki(url):

    headers = {
        'x-cisco-meraki-api-key': meraki_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(headers=headers, url=url)
    return response


def org_ids():
    url = f"{base_url}/organizations"
    response = get_meraki(url).json()
    id = response[0]['id']
    return id


def networks():
    networks = []
    url = f"{base_url}/organizations/{org_ids()}/networks"
    response = get_meraki(url).json()
    for network in response:
        networks.append(network)

    return networks


def clients():
    for network in networks():
        network_name = network['name']
        network_id = network["id"]
        url = f"{base_url}/networks/{network_id}/clients"
        response = get_meraki(url).json()
        for client in response:
            pprint(client)
            last_seen = client['lastSeen']
            print(last_seen)

clients()



