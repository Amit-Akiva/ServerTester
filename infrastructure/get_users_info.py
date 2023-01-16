import json

# 'C:/Users/amitak/PycharmProjects/song-server/users.json'


def load_user_data(loc):
    f = open(loc)
    return json.load(f)


def names(u_data):
    return list(u_data)


def fields_for_users(dict_in, name_in):
    return dict_in.get(name_in)
