def find_params(coords, spn, mode, point):
    toponym_longitude, toponym_lattitude = coords
    if point:
        org_point = "{0},{1}".format(toponym_longitude, toponym_lattitude)
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([str(spn), str(spn)]),
            "l": mode,
            "pt": "{0},pm2dgl".format(org_point)
        }
    else:
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([str(spn), str(spn)]),
            "l": mode
        }

    return map_params
