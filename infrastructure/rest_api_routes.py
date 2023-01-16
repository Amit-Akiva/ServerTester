import configparser
import connexion
import requests
import os
from definitions import ROOT_DIR

config = configparser.ConfigParser()
# os.path.join(ROOT_DIR, 'sources\\config.ini')
# config.read('/sources/config.ini')
config.read(os.path.join(ROOT_DIR, 'song-server-swagger\\sources\\config.ini')) # changed to relative path to run from test folder
host = config['target']['host']
port = config['target']['port']
target = 'http://' + host + ':' + port


def add_user(user_in):
    #r = requests.post(url=target + '/users/add_user', json=connexion.request.json)
    r = requests.post(url=target + '/users/add_user', json=user_in)
    # print(r)
    return r.json()


def get_user(user_param):
    #r = requests.get(url=target + '/users/get_user', params={'user_name': connexion.request.args['user_name']})
    r = requests.get(url=target + '/users/get_user', params={'user_name': user_param})
    # print(r.request.url)
    return r.json()

def get_song():
    r = requests.get(url=target + '/songs/get_song', params={'song_title': connexion.request.args['song_title']})
    return r.json()

def get_playlist():
    r = requests.get(url=target + '/users/get_playlist', params={'user_name': connexion.request.args['user_name'],
                                                            'user_password': connexion.request.args['user_password'],
                                                            'playlist_name': connexion.request.args['playlist_name']})
    return r.json()


def add_friend(user, password, friend_to_add):
    bod = {
        "friend_name": friend_to_add,
        "user_name": user,
        "user_password": password
    }
    r = requests.put(url=target + '/users/add_friend', json=bod)
    return r.json()


def change_password():
    r = requests.put(url=target + '/users/change_password', json=connexion.request.json)
    return r.json()


def add_playlist():
    r = requests.post(url=target + '/users/add_playlist', json=connexion.request.json)
    return r.json()


def add_song():
    r = requests.post(url=target + '/songs/add_song', json=connexion.request.json)
    return r.json()


def song_upvote():
    r = requests.put(url=target + '/songs/upvote', json=connexion.request.json)
    return r.json()


def song_downvote():
    r = requests.put(url=target + '/songs/downvote', json=connexion.request.json)
    return r.json()


def ranked_songs(rank='0-100', option='eq,less,greater'):
    payload = {'rank': rank, 'op': option}
    # payload = {'rank': connexion.request.args['rank'], 'op': connexion.request.args['op']}
    r = requests.get(url=target + '/songs/ranked_songs', params=payload)
    return r.json()


def playlist_add_song():
    r = requests.post(url=target + '/playlists/add_song', json=connexion.request.json)
    return r.json()


def delete_all_users():
    r = requests.delete(target + '/admin/delete_all_users')
    return r.json()


def delete_all_songs():
    r = requests.delete(target + '/admin/delete_all_songs')
    return r.json()


def set_songs():
    r = requests.post(url=target + '/admin/set_songs', json=connexion.request.json)
    return r.json()


def set_users():
    r = requests.post(url=target + '/admin/set_users', json=connexion.request.json)
    return r.json()
