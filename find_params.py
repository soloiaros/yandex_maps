def find_params(coords):

    toponym_longitude, toponym_lattitude = coords

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(['0.005', '0.005']),
        "l": "map",
    }

    return map_params
