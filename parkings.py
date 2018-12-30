APP_ID = ''
API_VERSION = 'v2.1'
BASE_URL = f'http://data.goteborg.se/ParkingService/{API_VERSION}/PublicTollParkings/{APP_ID}'

LONGITUDE, LATITUDE, RADIUS = 57.708314, 11.973153, 20 
GEO_ARGS = f'?latitude={LATITUDE}&longitude={LONGITUDE}&radius={RADIUS}'


def get_parkings():
    import requests
    import pandas as pd
    
    url = BASE_URL +  GEO_ARGS + '&format=Json'
    print(url)
    r = requests.get(url)
    
    if r.status_code == 200:
        data = r.json()     # convert to json (dict)
    else:
        # print('ERROR: ', r.status_code)
        data = None
        
    return data
        
        
# def get_available_spaces(id):
#     
#     return None
