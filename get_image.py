import sys
from io import BytesIO
import requests
from PIL import Image
from find_params import find_params


def get_image(coords, spn, mode, point=False):
    map_params = find_params(coords, spn, mode, point)
    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    Image.open(BytesIO(response.content)).save('data/map.png')
