import requests
from config import MAPS_API


def coords_from_address(address):
    search_params = {
        "apikey": MAPS_API,
        "geocode": address,
        "lang": "ru",
        "format": "json"
    }

    api_server = 'https://geocode-maps.yandex.ru/1.x'
    response = requests.get(api_server, params=search_params).json()
    object_json = response['response']['GeoObjectCollection']['featureMember'][0]
    lower_corner = object_json['GeoObject']['boundedBy']['Envelope']['lowerCorner'].split()
    upper_corner = object_json['GeoObject']['boundedBy']['Envelope']['upperCorner'].split()
    med_longitude = str((float(lower_corner[0]) + float(upper_corner[0])) / 2)
    med_latitude = str((float(upper_corner[1]) + float(lower_corner[1])) / 2)

    return med_longitude, med_latitude
