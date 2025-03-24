#Imports
import requests
import json

#Constants

TIMEOUT = 5 # 5 sec timeout
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://www.nasaspaceflight.com/',
    'Origin': 'https://www.nasaspaceflight.com',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
}

#function to get launches
#returns a success or failure message. Launch data if success and code data if failure
def GetLaunches() -> list:
    response = requests.get('https://nextspaceflight.com/launches/nsf_launches/10/', headers=HEADERS,timeout=TIMEOUT)
    #response = requests.get('https://httpbin.org/status/404')
    httpcode = response.status_code
    #debug network info here
    launchdata = response.json()
    return launchdata

data = GetLaunches()
print(json.dumps(data,indent=4))