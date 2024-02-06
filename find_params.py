def find_params(coords):

    toponym_longitude, toponym_lattitude = coords

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join(['0.05', '0.05']),
        "l": "map",
    }

    return map_params
