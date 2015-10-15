"""Test script for python-syncope"""
import sys
import os
import pytest
my_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, my_path + '/../')

import syncope


def test___init__syncope_url():
    """ Will test __init__ function if syncope_url is provided.

    :return:
    """
    with pytest.raises(ValueError) as excinfo:
        syn = syncope.Syncope(username="admin", password="password")
    assert excinfo.value.message == 'This interface needs an Syncope URL to work!'


def test___init__username():
    """ Will test __init__ function if username is provided.

    :return:
    """
    with pytest.raises(ValueError) as excinfo:
        syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", password="admin")
    assert excinfo.value.message == 'This interface needs an username to work!'


def test___init__password():
    """ Will test __init__ function if password is provided.

    :return:
    """
    with pytest.raises(ValueError) as excinfo:
        syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin")
    assert excinfo.value.message == 'This interface needs an password to work!'


def test__post():
    """ Will test __init__ function.
    :return:
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="admin")
    with pytest.raises(ValueError) as excinfo:
        data = syn._post("/syncope/cxf/users")
    assert excinfo.value.message == 'No arguments are given to POST.'


def test_get_users_count():
    """Will count the amount of users stored in the Syncope database.

    :return: Should return: 5
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    assert syn.get_users_count() == 5


def test_get_user_by_id():
    """Will get all information for user with id: 5.

    :return: Should return: puccini
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.get_user_by_id(5)
    username = user_data['username']
    assert username == "puccini"


def test_get_users_id_false():
    """Will get all information for user with id: 15.

    :return: Should return: False.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    assert syn.get_user_by_id(15) == False


def test_get_users_by_query():
    """Will search on username to find "vivaldi"

    :return: Should return: vivaldi
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
    user_data = syn.get_users_by_query(search_req)
    username = user_data[0]['username']
    assert username == "vivaldi"


def test_get_user_count_by_query():
    """Will count the amount of user which has 'vivaldi' as username.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
    assert syn.get_user_count_by_query(search_req) == 1


def test_get_user_by_name():
    """Will get all information for user with username: vivaldi

    :return: Should return: 3
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.get_user_by_name("vivaldi")
    assert user_data['id'] == 3


def test_get_paged_users_by_query():
    """Will search for all active users and return 1 user per page, getting the first page.

    :return: Should return: rossini
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"status","expression":"active"}}'
    user_data = syn.get_paged_users_by_query(search_req, 1, 1)
    username = user_data[0]['username']
    assert username == "rossini"


def test_suspend_user_by_id():
    """Will suspend the user for user id 1.

    :return: Should return: suspended
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.suspend_user_by_id(1)
    assert user_data['status'] == "suspended"


def test_reactivate_user_by_id():
    """Will reactivate the user for user id 1.

    :return: Should return: active
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.reactivate_user_by_id(1)
    assert user_data['status'] == "active"


def test_suspend_user_by_name():
    """Will suspend the user for user username vivaldi.

    :return: Should return: suspended
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.suspend_user_by_name("vivaldi")
    assert user_data['status'] == "suspended"


def test_reactivate_user_by_name():
    """Will reactivate the user for user username vivaldi.

    :return: Should return: active
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.reactivate_user_by_name("vivaldi")
    assert user_data['status'] == "active"


def test_create_user():
    """Will create an user weedijkerman

    :return: Should return: weedijkerman
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    create_user = '{"attributes": [{"schema": "aLong","values": [],"readonly": false},{"schema": "activationDate","values": [""],"readonly": false},{"schema": "cool","values": ["false"],"readonly": false},{"schema": "email","values": ["ikben@werner-dijkerman.nlx"],"readonly": false},{"schema": "firstname","values": ["Werner"],"readonly": false},{"schema": "fullname","values": ["Werner Dijkerman"],"readonly": false},{"schema": "gender","values": ["M"],"readonly": false},{"schema": "loginDate","values": [""],"readonly": false},{"schema": "makeItDouble","values": [],"readonly": false},{"schema": "surname","values": ["Dijkerman"],"readonly": false},{"schema": "type","values": ["account"],"readonly": false},{"schema": "uselessReadonly","values": [""],"readonly": true},{"schema": "userId","values": ["werner@dj-wasabi.nl"],"readonly": false}],"id": 0,"derivedAttributes": [{"schema": "cn","values": [],"readonly": false}],"virtualAttributes": [],"password": "password1234","status": null,"token": null,"tokenExpireTime": null,"username": "weedijkerman","lastLoginDate": null,"creationDate": null,"changePwdDate": null,"failedLogins": null}'
    user_data = syn.create_user(create_user)
    assert user_data['username'] == "weedijkerman"


def test_update_user():
    """Will update the user weedijkerman to wdijkerman.

    :return: Should return: wdijkerman
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.get_user_by_name("weedijkerman")
    user_id = int(user_data['id'])
    update_user = '{"id":' + str(user_id) + ',"attributesToBeUpdated":[{"schema":"uselessReadonly","valuesToBeAdded":[],"valuesToBeRemoved":[]},{"schema":"loginDate","valuesToBeAdded":[],"valuesToBeRemoved":[]},{"schema":"activationDate","valuesToBeAdded":[],"valuesToBeRemoved":[]}],"attributesToBeRemoved":["aLong","makeItDouble"],"derivedAttributesToBeAdded":[],"derivedAttributesToBeRemoved":[],"virtualAttributesToBeUpdated":[],"virtualAttributesToBeRemoved":[],"resourcesToBeAdded":[],"resourcesToBeRemoved":[],"password":null,"username":"wdijkerman","membershipsToBeAdded":[],"membershipsToBeRemoved":[],"pwdPropRequest":{"resources":[],"onSyncope":false}}'
    user_data = syn.update_user(update_user)
    assert user_data['username'] == "wdijkerman"


def test_delete_user_by_id():
    """Will delete the user with username wdijkerman.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.get_user_by_name("wdijkerman")
    user_id = int(user_data['id'])
    print str(user_id)
    assert syn.delete_user_by_id(user_id) == True


def test_get_users():
    """Will test to get all users.

    :return: Should return: 5
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    user_data = syn.get_users()
    assert len(user_data) == 5


# def test_create_users_to_enable():
#     syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
#     create_user = '{"attributes": [{"schema": "aLong","values": [],"readonly": false},{"schema": "activationDate","values": [1420074061],"readonly": false},{"schema": "cool","values": ["false"],"readonly": false},{"schema": "email","values": ["ikben@werner-dijkerman.nlx"],"readonly": false},{"schema": "firstname","values": ["Werner"],"readonly": false},{"schema": "fullname","values": ["Werner Dijkerman"],"readonly": false},{"schema": "gender","values": ["M"],"readonly": false},{"schema": "loginDate","values": [""],"readonly": false},{"schema": "makeItDouble","values": [],"readonly": false},{"schema": "surname","values": ["Dijkerman"],"readonly": false},{"schema": "type","values": ["account"],"readonly": false},{"schema": "uselessReadonly","values": [""],"readonly": true},{"schema": "userId","values": ["werner@dj-wasabi.nl"],"readonly": false}],"id": 0,"derivedAttributes": [{"schema": "cn","values": [],"readonly": false}],"virtualAttributes": [],"password": "password1234","status": null,"token": null,"tokenExpireTime": null,"username": "wdijkerman","lastLoginDate": null,"creationDate": null,"changePwdDate": null,"failedLogins": null}'
#     user_data = syn.create_users(create_user)
#     assert user_data['username'] == "wdijkerman"

def test_get_roles():
    """Will test to get all roles.

    :return: Should return: 5
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    roles_data = syn.get_roles()
    assert len(roles_data) == 14

def test_get_role_by_id():
    """Will get all information for user with id: 2.

    :return: Should return: puccini
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_role_by_id(2)
    role_name = role_data['name']
    assert role_name == "child"