"""Test script for python-syncope"""

import sys
import os
import pytest
import xml.etree.ElementTree as ET

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

    :return: Should return: 14
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    roles_data = syn.get_roles()
    assert len(roles_data) == 14


def test_get_roles_false():
    """Will test to get all roles. (Wrong password)

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    roles_data = syn.get_roles()
    assert roles_data == False


def test_get_role_by_id():
    """Will get all information for the role with id: 2.

    :return: Should return: child
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_role_by_id(2)
    role_name = role_data['name']
    assert role_name == "child"


def test_get_role_by_id_false():
    """Will get all information for the role with id: 22.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_role_by_id(22)
    assert role_data == False


def test_get_role_by_id_raise():
    """ Will test if an id is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_role_by_id()
    assert excinfo.value.message == 'This search needs an id to work!'


def test_get_parent_role_by_id():
    """Will get all information for role with id: 2.

    :return: Should return: root
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_parent_role_by_id(2)
    role_name = role_data['name']
    assert role_name == "root"


def test_get_parent_role_by_id_false():
    """Will get all parent information for role with id: 21.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_parent_role_by_id(21)
    assert role_data == False


def test_get_parent_role_by_id_raise():
    """ Will test if an id is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_parent_role_by_id()
    assert excinfo.value.message == 'This search needs an id to work!'


def test_get_children_role_by_id():
    """Will get all children information for role with id: 4.

    :return: Should return: secretary
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_children_role_by_id(4)
    role_name = role_data[0]['name']
    assert role_name == "secretary"


def test_get_children_role_by_id_false():
    """Will get all children information for role with id: 24.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    role_data = syn.get_children_role_by_id(24)
    assert role_data == False


def test_get_children_role_by_id_raise():
    """ Will test if an id is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_children_role_by_id()
    assert excinfo.value.message == 'This search needs an id to work!'


def test_create_role():
    """Will create an role with name 'my_new_role'.

    :return: Should return: secretary
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    my_role = '{"attributes":[{"schema":"icon","values":[],"readonly":false},{"schema":"rderived_dx","values":[],"readonly":false},{"schema":"rderived_sx","values":[],"readonly":false},{"schema":"show","values":["false"],"readonly":false},{"schema":"title","values":["My new attribute Title."],"readonly":false}],"id":0,"derivedAttributes":[],"virtualAttributes":[],"resources":["ws-target-resource-2","ws-target-resource-1"],"propagationStatusTOs":[],"name":"my_new_role","parent":1,"userOwner":null,"roleOwner":null,"inheritOwner":true,"inheritAttributes":false,"inheritDerivedAttributes":false,"inheritVirtualAttributes":false,"inheritPasswordPolicy":false,"inheritAccountPolicy":false,"entitlements":["CONFIGURATION_CREATE","CONFIGURATION_DELETE"],"passwordPolicy":4,"accountPolicy":6}'
    role_data = syn.create_role(my_role)
    role_name = role_data['name']
    assert role_name == "my_new_role"


def test_create_role_false():
    """Will create an rolec

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    my_role = '{}'
    role_data = syn.create_role(my_role)
    assert role_data == False


def test_create_role_raise():
    """ Will test if an JSON is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_role()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_update_role():
    """Will update the role created in previous test.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    roles_data = syn.get_roles()
    for role in roles_data:
        if role['name'] == 'my_new_role':
            role_id = role['id']
    my_role = '{"id":' + str(role_id) + ',"attributesToBeUpdated":[],"attributesToBeRemoved":["icon","rderived_sx","rderived_dx"],"derivedAttributesToBeAdded":[],"derivedAttributesToBeRemoved":[],"virtualAttributesToBeUpdated":[],"virtualAttributesToBeRemoved":[],"resourcesToBeAdded":[],"resourcesToBeRemoved":["ws-target-resource-2"],"name":"my_new_role_upd","userOwner":{"id":null},"roleOwner":{"id":null},"inheritOwner":true,"inheritAttributes":false,"inheritDerivedAttributes":false,"inheritVirtualAttributes":false,"inheritAccountPolicy":false,"inheritPasswordPolicy":false,"entitlements":["CONFIGURATION_CREATE","CONFIGURATION_DELETE","CONFIGURATION_UPDATE"],"passwordPolicy":{"id":4},"accountPolicy":{"id":6}}'
    role_upd_data = syn.update_role(my_role)

    role_name = role_upd_data['name']
    assert role_name == 'my_new_role_upd'


def test_update_role_false():
    """Will update the role created in previous test, but no correct JSON was given as argument.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    my_role = '{}'
    assert syn.update_role(my_role) == False


def test_update_role_railse():
    """Will update the role created in previous test.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.update_role()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_delete_role():
    """Will delete the role created in previous test.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    roles_data = syn.get_roles()

    for role in roles_data:
        if role['name'] == 'my_new_role_upd':
            role_id = role['id']
    assert syn.delete_role_by_id(role_id) == True


def test_delete_role_false():
    """Will delete the a non existing role.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    assert syn.delete_role_by_id(9999999) == False


def test_delete_role_raise():
    """ Will test if an id is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_role_by_id()
    assert excinfo.value.message == 'This search needs an id to work!'


def test_get_log_levels():
    """Will test to get all log levels.

    :return: Should return: 17
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    roles_data = syn.get_log_levels()
    assert len(roles_data) == 17


def test_get_log_levels_false():
    """Will test to get all log levels (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    roles_data = syn.get_log_levels()
    assert roles_data == False


def test_get_log_level_by_name():
    """Will get all information from log level where name is "ROOT".

    :return: Should return: "INFO"
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    log_level = syn.get_log_level_by_name("ROOT")
    log_level = log_level['level']
    assert log_level == "INFO"


def test_get_log_level_by_name_false():
    """Will get all information from non existing log name.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    log_level = syn.get_log_level_by_name("SYNCOPE")
    assert log_level == False


def test_get_log_level_by_name_raise():
    """ Will test if an name is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_log_level_by_name()
    assert excinfo.value.message == 'This search needs log level name to work!'


def test_create_or_update_log_level_update():
    """Will update the log level to "WARN".

    :return: Should return: "WARN"
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    update_log_level = '{"name": "org.apache.http", "level": "WARN"}'
    log_level = syn.create_or_update_log_level(update_log_level)
    assert log_level['level'] == "WARN"


def test_create_or_update_log_level_create():
    """Will create an new loglevel named 'SYNCOPE' with level 'WARN'.

    :return: Should return: json string
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    update_log_level = '{"name": "SYNCOPE", "level": "WARN"}'
    log_level = syn.create_or_update_log_level(update_log_level)
    assert log_level == {'level': 'WARN', 'name': 'SYNCOPE'}


def test_create_or_update_log_level_false_empty():
    """Will create an new log level, without JSON data.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    update_log_level = '{}'
    log_level = syn.create_or_update_log_level(update_log_level)
    assert log_level == False


def test_create_or_update_log_level_create_false():
    """Will create an new loglevel named 'SYNCOPE' with level 'WARN' (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="pasword")
    update_log_level = '{"name": "SYNCOPE", "level": "WARN"}'
    log_level = syn.create_or_update_log_level(update_log_level)
    assert log_level == False


def test_create_or_update_log_level_raise():
    """ Will test if an name is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_or_update_log_level()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_delete_log_level_by_name():
    """Will delete an log level with name "SYNCOPE".

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    assert syn.delete_log_level_by_name("SYNCOPE") == True


def test_delete_log_level_by_name_false():
    """Will delete an log level with non existing name "SYNCOPE_AGAIN".

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    assert syn.delete_log_level_by_name("SYNCOPE_AGAIN") == False


def test_delete_log_level_by_name_raise():
    """ Will test if an name is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_log_level_by_name()
    assert excinfo.value.message == 'This search needs log level name to work!'


def test_get_audit():
    """Will get all audit rules.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    audit_rules = syn.get_audit()
    assert len(audit_rules) == 1


def test_get_audit_false():
    """Will get all audit rules (Wrong password).

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="pasword")
    assert syn.get_audit() == False


def test_create_audit():
    """Will create an audit rule.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    add_audit_rule = '{"type":"REST","category":"LoggerController","subcategory":null,"event":"listAudits","result":"SUCCESS"}'
    assert syn.create_audit(add_audit_rule) == True


def test_create_audit_false():
    """Will create an audit rule.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    add_audit_rule = ''
    assert syn.create_audit(add_audit_rule) == False


def test_create_audit_raise():
    """Will create an audit rule.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_audit()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_delete_audit():
    """Will delete an audit rule.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    delete_audit_rule = '{"type":"REST","category":"LoggerController","subcategory":null,"event":"listAudits","result":"SUCCESS"}'
    assert syn.delete_audit(delete_audit_rule) == True


def test_delete_audit_false():
    """Will delete an audit rule.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    delete_audit_rule = ''
    assert syn.delete_audit(delete_audit_rule) == False


def test_create_audit_raise():
    """ Will test if an name is given as argument.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_audit()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_get_configurations():
    """Will test to get all configurations.

    :return: Should return: 10
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_configurations()
    assert len(resource_data) == 10


def test_get_configurations_false():
    """Will test to get all configurations (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_configurations() == False


def test_get_configuration_by_key():
    """Will test to get all configuration by key.

    :return: Should return: {'key': 'password.cipher.algorithm', 'value': 'SHA1'}
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_configuration_by_key("password.cipher.algorithm")
    assert resource_data == {'key': 'password.cipher.algorithm', 'value': 'SHA1'}


def test_get_configuration_by_key_false():
    """Will test to get configuration by key (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_configuration_by_key("password.cipher.algorithm") == False


def test_get_configuration_by_key_raise():
    """Will test to get configuration by key without key.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_configuration_by_key()
    assert excinfo.value.message == 'This search needs an configuration key to work!'


def test_create_configuration():
    """Will create an configuration.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    create_configuration = '{"key": "my.path", "value": "/opt/path"}'
    resource_data = syn.create_configuration(create_configuration)
    assert resource_data == True


def test_create_configuration_false():
    """Will create an configuration (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    create_configuration = '{"key": "my.path", "value": "/opt/path"}'
    assert syn.create_configuration(create_configuration) == False


def test_create_configuration_raise():
    """Will create an configuration without json data.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_configuration()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_update_configuration():
    """Will update the configuration.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    update_configuration = '{"key": "my.path", "value": "/opt/newpath"}'
    resource_data = syn.update_configuration(update_configuration)
    assert resource_data == True


def test_update_configuration_false():
    """Will update the configuration (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    update_configuration = '{"key": "my.path", "value": "/opt/newpath"}'
    assert syn.update_configuration(update_configuration) == False


def test_update_configuration_false_json():
    """Will update the configuration, with "faulty" json data.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    update_configuration = '{"keys": "my.path", "values": "/opt/newpath"}'
    assert syn.update_configuration(update_configuration) == False


def test_update_configuration_raise():
    """Will update the configuration, without json data.

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.update_configuration()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_delete_configuration_by_key():
    """Will delete an configuration.

    :return: Should return: true
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.delete_configuration_by_key("my.path")
    assert resource_data == True


def test_delete_configuration_by_key_false():
    """Will delete an configuration (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.delete_configuration_by_key("my.path") == False


def test_delete_configuration_by_key_raise():
    """Will delete an configuration without key name.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_configuration_by_key()
    assert excinfo.value.message == 'This search needs JSON data to work!'


def test_get_configuration_validators():
    """Will test to get all configuration validators.

    :return: Should return: 10
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_configuration_validators()
    assert len(resource_data) == 3


def test_get_configuration_validators_false():
    """Will test to get all configuration validators (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_configuration_validators() == False


def test_get_configuration_mailtemplates():
    """Will test to get all mailtemplates.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_configuration_mailtemplates()
    assert len(resource_data) == 1


def test_get_configuration_mailtemplates_false():
    """Will test to get all mailtemplates (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_configuration_mailtemplates() == False


def test_get_configuration_stream():
    """Will test to get configuration stream.

    :return: Should return: dataset
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_configuration_stream()
    tree = ET.fromstring(resource_data.text)
    assert tree.tag == "dataset"


def test_get_configuration_stream_false():
    """Will test to get configuration stream (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_configuration_stream() == False


def test_get_entitlements():
    """Will return a list of all known entitlements.

    :return: Should return: dataset
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_entitlements()
    assert len(resource_data) == 84


def test_get_entitlements_false():
    """Will return a list of all known entitlements (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_entitlements() == False


def test_get_own_entitlements():
    """Will return a list of all known entitlements.

    :return: Should return: 84
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    resource_data = syn.get_own_entitlements()
    assert len(resource_data) == 84


def test_get_own_entitlements_false():
    """Will return a list of all known entitlements (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_own_entitlements() == False


def test_get_notifications():
    """Will return a list of all notifications.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    notification_data = syn.get_notifications()
    assert len(notification_data) == 1


def test_get_notifications_false():
    """Will return a list of all notifications (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_notifications() == False


def test_get_notification_by_id():
    """Will return information for notifications with id.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    notification_data = syn.get_notification_by_id(1)
    assert len(notification_data) == 11


def test_get_notification_by_id_false():
    """Will return information for notifications with id (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_notification_by_id(1) == False


def test_get_notification_by_id_raise():
    """Will return information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_notification_by_id()
    assert excinfo.value.message == 'This search needs an id to work!'


def test_create_notification():
    """Will create an notification

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    create_notification = '{"events":["[REST]:[LoggerController]:[]:[deleteLog]:[SUCCESS]","[REST]:[LoggerController]:[]:[disableAudit]:[SUCCESS]"],"recipientAttrType":"Username","recipientAttrName":"Username","selfAsRecipient":true,"sender":"me@home.nl","subject":"this is very important","template":"optin","traceLevel":"FAILURES"}'
    notification_data = syn.create_notification(create_notification)
    assert notification_data == True


def test_create_notification_false():
    """Will create an notification (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    create_notification = '{"events":["[REST]:[LoggerController]:[]:[deleteLog]:[SUCCESS]","[REST]:[LoggerController]:[]:[disableAudit]:[SUCCESS]"],"recipientAttrType":"Username","recipientAttrName":"Username","selfAsRecipient":true,"sender":"me@home.nl","subject":"this is very important","template":"optin","traceLevel":"FAILURES"}'
    notification_data = syn.create_notification(create_notification)
    assert notification_data == False


def test_create_notification_raise():
    """Will return information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_notification()
    assert excinfo.value.message == 'This search needs an JSON to work!'


def test_update_notification_by_id():
    """Will update an notification

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    # Get latest notification_id
    notifications_list = []
    for notification in syn.get_notifications():
        notifications_list.append(notification['id'])
    notifications_list.reverse()
    notifications_id =  notifications_list[0]
    update_notification = '{"id":' + str(notifications_id) + ',"events":["[REST]:[LoggerController]:[]:[deleteLog]:[SUCCESS]"],"about":null,"recipients":null,"recipientAttrType":"Username","recipientAttrName":"Username","selfAsRecipient":true,"sender":"me@home.nl","subject":"this is very important again","template":"optin","traceLevel":"FAILURES"}'
    notification_data = syn.update_notification_by_id(update_notification)
    assert notification_data == True


def test_update_notification_by_id_false():
    """Will update an notification (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    create_notification = '{"events":["[REST]:[LoggerController]:[]:[deleteLog]:[SUCCESS]","[REST]:[LoggerController]:[]:[disableAudit]:[SUCCESS]"],"recipientAttrType":"Username","recipientAttrName":"Username","selfAsRecipient":true,"sender":"me@home.nl","subject":"this is very important","template":"optin","traceLevel":"FAILURES"}'
    notification_data = syn.update_notification_by_id(create_notification)
    assert notification_data == False


def test_update_notification_by_id_raise():
    """Will update information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.update_notification_by_id()
    assert excinfo.value.message == 'This search needs an JSON to work!'


def test_datele_notification_by_id():
    """Will delete an notification

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    # Get latest notification_id
    notifications_list = []
    for notification in syn.get_notifications():
        notifications_list.append(notification['id'])
    notifications_list.reverse()
    notifications_id =  notifications_list[0]
    notification_data = syn.delete_notification_by_id(notifications_id)
    assert notification_data == True


def test_delete_notification_by_id_false():
    """Will delete an notification (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    notification_data = syn.delete_notification_by_id(101)
    assert notification_data == False


def test_delete_notification_by_id_raise():
    """Will delete information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_notification_by_id()
    assert excinfo.value.message == 'This search needs an JSON to work!'


def test_get_account_policies():
    """Will return a list of account policies.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    account_policies_data = syn.get_account_policies()
    assert len(account_policies_data) == 1


def test_get_account_policies_false():
    """Will return a list of account policies (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_account_policies() == False


def test_get_account_policy_by_id():
    """Will return a list of account policies.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    account_policies_data = syn.get_account_policy_by_id(5)
    account_policies_data_type = account_policies_data['type']
    assert account_policies_data_type == "GLOBAL_ACCOUNT"


def test_get_account_policy_by_id_false():
    """Will return a list of account policies (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_account_policy_by_id(5) == False


def test_get_account_policy_by_id_raise():
    """Will update information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_account_policy_by_id()
    assert excinfo.value.message == 'This needs an ID to work!'


def test_create_account_policy():
    """Will create an account policy.

    :return: Should return: ACCOUNT
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    create_account_policy = '{"description":"My Description","type":"ACCOUNT","usedByResources":[],"usedByRoles":[],"specification":{"maxLength":0,"minLength":0,"pattern":null,"wordsNotPermitted":[],"schemasNotPermitted":["firstname","email"],"prefixesNotPermitted":[],"suffixesNotPermitted":[],"allUpperCase":false,"allLowerCase":false,"propagateSuspension":false,"permittedLoginRetries":0}}'
    account_policy_data = syn.create_account_policy(create_account_policy)
    account_policy_type = account_policy_data['type']
    assert account_policy_type == "ACCOUNT"


def test_create_account_policy_false():
    """Will create an account policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.create_account_policy("json") == False


def test_create_account_policy_raise():
    """Will create an account policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_account_policy()
    assert excinfo.value.message == 'This create needs an JSON to work!'


def test_update_account_policy():
    """Will update an account policy.

    :return: Should return: secretary
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")

    account_policies_list = []
    for policy in syn.get_account_policies():
        account_policies_list.append(policy['id'])
    account_policies_list.reverse()
    policy_id =  account_policies_list[0]
    update_policy = '{"id":' + str(policy_id) + ',"description":"My Description 2","type":"ACCOUNT","usedByResources":[],"usedByRoles":[],"specification":{"maxLength":0,"minLength":0,"pattern":null,"wordsNotPermitted":[],"schemasNotPermitted":["firstname"],"prefixesNotPermitted":[],"suffixesNotPermitted":[],"allUpperCase":false,"allLowerCase":false,"propagateSuspension":false,"permittedLoginRetries":0}}'
    account_policy_data = syn.update_account_policy(update_policy)
    account_policy_type = account_policy_data['type']
    assert account_policy_type == "ACCOUNT"


def test_update_account_policy_false():
    """Will update an account policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.update_account_policy("json") == False


def test_update_account_policy_raise():
    """Will update an account policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.update_account_policy()
    assert excinfo.value.message == 'This update needs an JSON to work!'


def test_delete_account_policy():
    """Will delete an account policy.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")

    account_policies_list = []
    for policy in syn.get_account_policies():
        account_policies_list.append(policy['id'])
    account_policies_list.reverse()
    policy_id =  account_policies_list[0]
    assert syn.delete_account_policy(policy_id) == True


def test_delete_account_policy_false():
    """Will delete an account policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.delete_account_policy("json") == False


def test_delete_account_policy_raise():
    """Will delete an account policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_account_policy()
    assert excinfo.value.message == 'This delete needs an id to work!'


def test_get_sync_policies():
    """Will return a list of sync policies.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    sync_policies_data = syn.get_sync_policies()
    assert len(sync_policies_data) == 3


def test_get_sync_policies_false():
    """Will return a list of sync policies (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_sync_policies() == False


def test_get_sync_policy_by_id():
    """Will return a list of sync policies.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    sync_policies_data = syn.get_sync_policy_by_id(5)
    sync_policies_data_type = sync_policies_data['type']
    assert sync_policies_data_type == "GLOBAL_ACCOUNT"


def test_get_sync_policy_by_id_false():
    """Will return a list of sync policies (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_sync_policy_by_id(5) == False


def test_get_sync_policy_by_id_raise():
    """Will update information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_sync_policy_by_id()
    assert excinfo.value.message == 'This needs an ID to work!'


def test_create_sync_policy():
    """Will create an sync policy.

    :return: Should return: ACCOUNT
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    create_sync_policy = '{"description":"My First Sync","type":"SYNC","usedByResources":[],"usedByRoles":[],"specification":{"uAltSearchSchemas":["loginDate"],"userJavaRule":null,"rAltSearchSchemas":[],"roleJavaRule":null,"conflictResolutionAction":"FIRSTMATCH"}}'
    sync_policy_data = syn.create_sync_policy(create_sync_policy)
    sync_policy_type = sync_policy_data['type']
    assert sync_policy_type == "SYNC"


def test_create_sync_policy_false():
    """Will create an sync policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.create_sync_policy("json") == False


def test_create_sync_policy_raise():
    """Will create an sync policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_sync_policy()
    assert excinfo.value.message == 'This create needs an JSON to work!'


def test_update_sync_policy():
    """Will update an sync policy.

    :return: Should return: secretary
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")

    sync_policies_list = []
    for policy in syn.get_sync_policies():
        sync_policies_list.append(policy['id'])
    sync_policies_list.reverse()
    policy_id =  sync_policies_list[0]
    update_policy = '{"id":' + str(policy_id) + ',"description":"My First Sync 2","type":"SYNC","usedByResources":[],"usedByRoles":[],"specification":{"uAltSearchSchemas":["loginDate","firstname"],"userJavaRule":null,"rAltSearchSchemas":[],"roleJavaRule":null,"conflictResolutionAction":"FIRSTMATCH"}}'
    sync_policy_data = syn.update_sync_policy(update_policy)
    sync_policy_type = sync_policy_data['type']
    assert sync_policy_type == "SYNC"


def test_update_sync_policy_false():
    """Will update an sync policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.update_sync_policy("json") == False


def test_update_sync_policy_raise():
    """Will update an sync policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.update_sync_policy()
    assert excinfo.value.message == 'This update needs an JSON to work!'


def test_delete_sync_policy():
    """Will delete an sync policy.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    sync_policies_list = []
    for policy in syn.get_sync_policies():
        sync_policies_list.append(policy['id'])
    sync_policies_list.reverse()
    policy_id = sync_policies_list[0]
    assert syn.delete_sync_policy(policy_id) == True


def test_delete_sync_policy_false():
    """Will delete an sync policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.delete_sync_policy("json") == False


def test_delete_sync_policy_raise():
    """Will delete an sync policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_sync_policy()
    assert excinfo.value.message == 'This delete needs an id to work!'

def test_get_password_policies():
    """Will return a list of password policies.

    :return: Should return: 2
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    password_policies_data = syn.get_password_policies()
    assert len(password_policies_data) == 2


def test_get_password_policies_false():
    """Will return a list of password policies (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_password_policies() == False


def test_get_password_policy_by_id():
    """Will return a list of password policies.

    :return: Should return: 1
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    password_policies_data = syn.get_password_policy_by_id(5)
    password_policies_data_type = password_policies_data['type']
    assert password_policies_data_type == "GLOBAL_ACCOUNT"


def test_get_password_policy_by_id_false():
    """Will return a list of password policies (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.get_password_policy_by_id(5) == False


def test_get_password_policy_by_id_raise():
    """Will update information for notifications with id.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.get_password_policy_by_id()
    assert excinfo.value.message == 'This needs an ID to work!'


def test_create_password_policy():
    """Will create an password policy.

    :return: Should return: ACCOUNT
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    create_password_policy = '{"description":"My Password Policy","type":"PASSWORD","usedByResources":[],"usedByRoles":[],"specification":{"historyLength":10,"maxLength":0,"minLength":8,"wordsNotPermitted":[],"schemasNotPermitted":[],"nonAlphanumericRequired":true,"alphanumericRequired":true,"digitRequired":true,"lowercaseRequired":false,"uppercaseRequired":false,"mustStartWithDigit":false,"mustntStartWithDigit":false,"mustEndWithDigit":false,"mustntEndWithDigit":false,"mustStartWithNonAlpha":false,"mustStartWithAlpha":false,"mustntStartWithNonAlpha":false,"mustntStartWithAlpha":false,"mustEndWithNonAlpha":false,"mustEndWithAlpha":false,"mustntEndWithNonAlpha":false,"mustntEndWithAlpha":false,"prefixesNotPermitted":[],"suffixesNotPermitted":[]}}'
    password_policy_data = syn.create_password_policy(create_password_policy)
    password_policy_type = password_policy_data['type']
    assert password_policy_type == "PASSWORD"


def test_create_password_policy_false():
    """Will create an password policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.create_password_policy("json") == False


def test_create_password_policy_raise():
    """Will create an password policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.create_password_policy()
    assert excinfo.value.message == 'This create needs an JSON to work!'


def test_update_password_policy():
    """Will update an password policy.

    :return: Should return: PASSWORD
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")

    password_policies_list = []
    for policy in syn.get_password_policies():
        password_policies_list.append(policy['id'])
    password_policies_list.reverse()
    policy_id = password_policies_list[0]
    update_policy = '{"id":' + str(policy_id) + ',"description":"My Password Policy 2","type":"PASSWORD","usedByResources":[],"usedByRoles":[],"specification":{"historyLength":10,"maxLength":0,"minLength":8,"wordsNotPermitted":[],"schemasNotPermitted":[],"nonAlphanumericRequired":true,"alphanumericRequired":true,"digitRequired":true,"lowercaseRequired":false,"uppercaseRequired":false,"mustStartWithDigit":false,"mustntStartWithDigit":false,"mustEndWithDigit":false,"mustntEndWithDigit":false,"mustStartWithNonAlpha":false,"mustStartWithAlpha":false,"mustntStartWithNonAlpha":false,"mustntStartWithAlpha":false,"mustEndWithNonAlpha":false,"mustEndWithAlpha":false,"mustntEndWithNonAlpha":false,"mustntEndWithAlpha":false,"prefixesNotPermitted":[],"suffixesNotPermitted":[]}}'
    password_policy_data = syn.update_password_policy(update_policy)
    password_policy_type = password_policy_data['type']
    assert password_policy_type == "PASSWORD"


def test_update_password_policy_false():
    """Will update an password policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.update_password_policy("json") == False


def test_update_password_policy_raise():
    """Will update an password policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.update_password_policy()
    assert excinfo.value.message == 'This update needs an JSON to work!'


def test_delete_password_policy():
    """Will delete an password policy.

    :return: Should return: True
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")

    password_policies_list = []
    for policy in syn.get_password_policies():
        password_policies_list.append(policy['id'])
    password_policies_list.reverse()
    policy_id =  password_policies_list[0]
    assert syn.delete_password_policy(policy_id) == True


def test_delete_password_policy_false():
    """Will delete an password policy (Wrong password).

    :return: Should return: False
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
    assert syn.delete_password_policy("json") == False


def test_delete_password_policy_raise():
    """Will delete an password policy.

    :return: Should catch the ValueError.
    """
    syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
    with pytest.raises(ValueError) as excinfo:
        syn.delete_password_policy()
    assert excinfo.value.message == 'This delete needs an id to work!'



# def test_get_resources():
#     """Will test to get all users.
#
#     :return: Should return: 5
#     """
#     syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="password")
#     resource_data = syn.get_resources()
#     assert len(resource_data) == 18
#
#
# def test_get_resources_false():
#     """Will test to get all users (Wrong password).
#
#     :return: Should return: False
#     """
#     syn = syncope.Syncope(syncope_url="http://192.168.1.145:9080", username="admin", password="passwrd")
#     assert syn.get_resources() == False


