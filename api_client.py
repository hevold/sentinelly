import requests
from datetime import datetime, timedelta
import config

def get_access_token():
    # Henter tilgangstoken fra Sentinel Hub
    response = requests.post(
        'https://services.sentinel-hub.com/oauth/token',
        data={
            'client_id': config.CLIENT_ID,
            'client_secret': config.CLIENT_SECRET,
            'grant_type': 'client_credentials'
        }
    )
    response.raise_for_status()
    return response.json()['access_token']

def get_image(coordinate, width=2048, height=2048):
    token = get_access_token()
    headers = {'Authorization': f'Bearer {token}'}

    lat, lng = coordinate
    buffer_size = 0.02  # Juster denne verdien for å endre omfanget av bbox
    bbox = f"{lng-buffer_size},{lat-buffer_size},{lng+buffer_size},{lat+buffer_size}"

    # Setter tidsintervallet til de siste 30 dagene
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    date_interval = f"{start_date.strftime('%Y-%m-%d')}/{end_date.strftime('%Y-%m-%d')}"

    # URL og parametere for WMS GetMap-forespørsel
    url = f"https://services.sentinel-hub.com/ogc/wms/{config.INSTANCE_ID}"
    params = {
        'service': 'WMS',
        'request': 'GetMap',
        'layers': 'TRUE-COLOR-S2L2A',  # Multispektrale lag (bånd)
        'styles': '',
        'format': 'image/jpeg',
        'transparent': 'true',
        'version': '1.1.1',
        'bbox': bbox,
        'srs': 'EPSG:4326',
        'width': width,
        'height': height,
        'time': date_interval
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Feil i forespørsel:")
        print(response.text)
        return None

    return response.content  # Dette er bildedataene

# Testkode

