"""Test script for python-syncope"""
import syncope


def test_get_users_count():
    """Will count the amount of users stored in the Syncope database. This would be: 5"""
    syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    assert syn.get_users_count() == 5


def test_get_users_search():
    """Will count the amount of user which has 'vivaldi' as username. This would be: 1"""
    syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
    assert syn.get_users_search_count(search_req) == 1


def test_get_users_id():
    """Will get all information for user with id: 5.

    :return: Should return the username: puccini
    """
    syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    user_data = syn.get_users_id(5)
    username = user_data['username']
    assert username == "puccini"


def test_get_users_id_false():
    """Will get all information for user with id: 15.

    :return: Should return false
    """
    syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    assert syn.get_users_id(15) == False

