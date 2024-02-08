def find_params(coords, spn):
    toponym_longitude, toponym_lattitude = coords
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(spn), str(spn)]),
        "l": "map",
    }

    return map_params
