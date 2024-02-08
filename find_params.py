def find_params(coords, spn, mode):
    toponym_longitude, toponym_lattitude = coords
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(spn), str(spn)]),
        "l": mode,
    }

    return map_params
