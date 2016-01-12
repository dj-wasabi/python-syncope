"""python-syncope is an python wrapper for the Syncope Rest API."""


__author__ = 'Werner Dijkerman'
__version__ = '0.0.6'
__license__ = "Apache License 2.0"
__email__ = "ikben@werner-dijkerman.nl"

import requests
import json


class Syncope(object):

    """Syncope Rest Interface."""

    def __init__(self, syncope_url='', username=None, password=None, timeout=10):
        """
        Will initialize the syncope module.

        :param syncope_url: the URL to the Syncope server.
        :param username: The username to login.
        :param password: The password for the user configured in username.
        :param timeout: HTTP requests timeout in seconds.
        """
        if not syncope_url:
            raise ValueError('This interface needs an Syncope URL to work!')

        if not username:
            raise ValueError('This interface needs an username to work!')

        if not password:
            raise ValueError('This interface needs an password to work!')

        self.syncope_url = syncope_url
        self.headers = {'Content-Type': 'application/json'}
        self.username = username
        self.password = password
        self.timeout = int(timeout)
        self.rest_configurations = 'syncope/cxf/configurations'
        self.cxf_account_policies = 'syncope/cxf/policies/account'
        self.cxf_sync_policies = 'syncope/cxf/policies/sync'
        self.cxf_password_policies = 'syncope/cxf/policies/password'
        self.rest_account_policies = 'syncope/rest/policy/account'
        self.rest_sync_policies = 'syncope/rest/policy/sync'
        self.rest_password_policies = 'syncope/rest/policy/password'
        self.rest_entitlements = 'syncope/cxf/entitlements'
        self.rest_logging = 'syncope/cxf/logger/normal'
        self.rest_log_audit = 'syncope/cxf/logger/audit'
        self.rest_notifications = 'syncope/cxf/notifications'
        self.rest_audit = 'syncope/cxf/audit'
        self.rest_connectors = 'syncope/cxf/connectors'
        self.rest_resources = 'syncope/cxf/resources'
        self.rest_roles = 'syncope/cxf/roles'
        self.rest_users = 'syncope/cxf/users'

    def _get(self, rest_path, arguments=None):
        """Will GET the information from the syncope server. This function will be called from the actual actions.

        :param rest_path: uri of the rest action.
        :param arguments: Optional arguments.
        :return: Returns the data in json from the GET request.
        """
        if arguments is not None:
            syncope_path = "{0}/{1}.json{2}".format(self.syncope_url, rest_path, arguments)
        else:
            syncope_path = "{0}/{1}.json".format(self.syncope_url, rest_path)

        return requests.get(syncope_path, auth=(self.username, self.password), headers=self.headers, timeout=self.timeout)

    def _get_xml(self, rest_path, arguments=None):
        """Will GET the information from the syncope server with XML. This function will be called from the actual actions.

        :param rest_path: uri of the rest action.
        :param arguments: Optional arguments.
        :return: Returns the data in XML from the GET request.
        """
        headers = {'Content-Type': 'application/xml'}
        if arguments is not None:
            syncope_path = "{0}/{1}{2}".format(self.syncope_url, rest_path, arguments)
        else:
            syncope_path = "{0}/{1}".format(self.syncope_url, rest_path)

        return requests.get(syncope_path, auth=(self.username, self.password), headers=headers, timeout=self.timeout)

    def _delete(self, rest_path, arguments=None):
        """Will DELETE the information from the syncope server. This function will be called from the actual actions.

        :param rest_path: uri of the rest action.
        :param arguments: Optional arguments.
        :return: Returns the data in json (if any) from the DELETE request.
        """
        syncope_path = "{0}/{1}.json".format(self.syncope_url, rest_path)

        return requests.delete(syncope_path, auth=(self.username, self.password), headers=self.headers, data=arguments, timeout=self.timeout)

    def _post(self, rest_path, arguments=None, params=None):
        """Will do an POST action for creating or to update the information from the syncope server. This function will be called from the actual actions.

        :param rest_path: uri of the rest action.
        :param arguments: Optional arguments in JSON format.
        :param params: Optional parameters to the uri, like: ?username=something.
        :return: Returns the data in json (if any)from the POST request.
        """
        if arguments is None:
            raise ValueError('No arguments are given to POST.')
        if params is not None:
            syncope_path = "{0}/{1}.json{2}".format(self.syncope_url, rest_path, params)
        else:
            syncope_path = "{0}/{1}.json".format(self.syncope_url, rest_path)

        try:
            data = requests.post(syncope_path, auth=(self.username, self.password), headers=self.headers, data=arguments, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            print e

        return data

    def _put(self, rest_path, arguments=None, params=None):
        """Will do an PUT action for creating or to update the information from the syncope server. This function will be called from the actual actions.

        :param rest_path: uri of the rest action.
        :param arguments: Optional arguments in JSON format.
        :param params: Optional parameters to the uri, like: ?username=something.
        :return: Returns the data in json (if any)from the POST request.
        """
        if arguments is None:
            raise ValueError('No arguments are given to PUT.')
        if params is not None:
            syncope_path = "{0}/{1}.json{2}".format(self.syncope_url, rest_path, params)
        else:
            syncope_path = "{0}/{1}.json".format(self.syncope_url, rest_path)

        return requests.put(syncope_path, auth=(self.username, self.password), headers=self.headers, data=arguments, timeout=self.timeout)

    def create_user(self, arguments):
        """Will create an user.

        :param arguments: An JSON structure for creating the user. An example can be found in the 'examples' folder.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the just created user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> create_user = '{"attributes": [{"schema": "aLong","values": [],"readonly": false},{"schema": "activationDate","values": [""],"readonly": false},{"schema": "cool","values": ["false"],"readonly": false},{"schema": "email","values": ["werner@dj-wasabi.nl"],"readonly": false},{"schema": "firstname","values": ["Werner"],"readonly": false},{"schema": "fullname","values": ["Werner Dijkerman"],"readonly": false},{"schema": "gender","values": ["M"],"readonly": false},{"schema": "loginDate","values": [""],"readonly": false},{"schema": "makeItDouble","values": [],"readonly": false},{"schema": "surname","values": ["Dijkerman"],"readonly": false},{"schema": "type","values": ["account"],"readonly": false},{"schema": "uselessReadonly","values": [""],"readonly": true},{"schema": "userId","values": ["werner@dj-wasabi.nl"],"readonly": false}],"id": 0,"derivedAttributes": [{"schema": "cn","values": [],"readonly": false}],"virtualAttributes": [],"password": "password1234","status": null,"token": null,"tokenExpireTime": null,"username": "wedijkerman","lastLoginDate": null,"creationDate": null,"changePwdDate": null,"failedLogins": null}'
        >>> print syn.create_users(create_user)
        {u'status': u'active', u'username': u'wedijkerman', u'creationDate': 1444152747171, <cut>}
        """

        data = self._post(self.rest_users, arguments)

        if data.status_code == 201:
            return data.json()
        else:
            return False

    def update_user(self, arguments):
        """Will update an user.

        :param arguments: An JSON structure for updating the user. An example can be found in the 'examples' folder.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the just updated user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_user = '{"id":137,"attributesToBeUpdated":[{"schema":"uselessReadonly","valuesToBeAdded":[],"valuesToBeRemoved":[]},{"schema":"loginDate","valuesToBeAdded":[],"valuesToBeRemoved":[]},{"schema":"activationDate","valuesToBeAdded":[],"valuesToBeRemoved":[]}],"attributesToBeRemoved":["aLong","makeItDouble"],"derivedAttributesToBeAdded":[],"derivedAttributesToBeRemoved":[],"virtualAttributesToBeUpdated":[],"virtualAttributesToBeRemoved":[],"resourcesToBeAdded":[],"resourcesToBeRemoved":[],"password":null,"username":"wdijkerman","membershipsToBeAdded":[],"membershipsToBeRemoved":[],"pwdPropRequest":{"resources":[],"onSyncope":false}}'
        >>> print syn.update_user(update_user)
        {u'status': u'active', u'username': u'wdijkerman', u'creationDate': 1444676322330, <cut>}
        """
        data = self._post("/syncope/rest/user/update", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users(self):
        """Get information from all users in JSON.

        :return: False when something went wrong, or json data with all information from all users.
        """
        data = self._get(self.rest_users)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_user_by_id(self, id=None):
        """Will get all data from specific user, specified via id.

        :param id: The id of the user to get information.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_user_by_id(5)
        {u'status': u'active', u'username': u'puccini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get(self.rest_users + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_by_query(self, arguments=None):
        """Will search an user. It will require an python dict to be used for the searching.

        :param arguments: An JSON structure. See example for more information.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the search request.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
        >>> print syn.get_users_by_query(search_req)
        {u'status': u'active', u'username': u'vivaldi', <cut>}
        >>> search_req = '{"type":"LEAF","resourceCond":{"resourceName":"ws-target-resource-1"}}'
        >>> print syn.get_users_by_query(search_req)
        {u'status': u'active', u'username': u'vivaldi', <cut>}
        """
        if arguments is None:
            raise ValueError('This search needs an dict to work!')

        data = self._post(self.rest_users +"/search", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_user_count_by_query(self, arguments=None):
        """Will count the users matching the search request.

        :param arguments: An JSON structure. See example for more information.
        :type arguments: JSON
        :return: False when something went wrong, or the amount of users matching the request.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
        >>> print syn.get_user_count_by_query(search_req)
        5
        >>> search_req = '{"type":"LEAF","resourceCond":{"resourceName":"ws-target-resource-1"}}'
        >>> print syn.get_user_count_by_query(search_req)
        1
        """
        if arguments is None:
            raise ValueError('This search needs an dict to work!')

        data = self._post(self.rest_users +"/search/count", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_paged_users_by_query(self, arguments=None, page=None, size=None):
        """Will search an user and will return the data by pages.

        :param arguments: An JSON structure. See example for more information.
        :type arguments: JSON
        :param page: The page it should return.
        :type page: int
        :param size: The amount of results per page.
        :type size: int
        :return: False when something went wrong, or json data with all information from the search request.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"status","expression":"active"}}'
        >>> print syn.get_paged_users_by_query(search_user, 1, 1)
        {u'status': u'active', u'username': u'rossini', <cut>}
        >>> print syn.get_paged_users_by_query(search_user, 3, 1)
        {u'status': u'active', u'username': u'vivaldi', <cut>}
        """
        if arguments is None:
            raise ValueError('This search needs an JSON to work!')
        if page is None:
            raise ValueError('This search needs an page to work!')
        if size is None:
            raise ValueError('This search needs an size to work!')

        data = self._post(self.rest_users +"/search", arguments, "?page=" + str(page) + "&size=" + str(size))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_user_by_name(self, username=None):
        """Will get all data from specific user, specified via username.

        :param username: The username of the user to get information.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_user_by_name("puccini")
        {u'status': u'active', u'username': u'puccini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')
        data = self._get(self.rest_users, "?username=" + str(username))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_count(self):
        """Will count all users found in Syncope and return an number.

        :return: False when something went wrong, or the amount of users.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_users_count()
        5
        """
        data = self._get(self.rest_users + "/count")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def enable_user_by_id(self, id=None):
        """Will activate an user.

        :param id: The id of the user to activate.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.enable_user_by_id(1)
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._post(self.rest_users + "/" + str(id) + "/status/activate", '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def enable_user_by_name(self, username=None):
        """Will activate an user.

        :param username: The username of the user to activate.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.enable_user_by_name("rossini")
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')

        data = self._post(self.rest_users + "/activateByUsername/" + username, '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def reactivate_user_by_id(self, id=None):
        """Will reactivate an user.

        :param id: The id of the user to reactivate.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.reactivate_user_by_id(1)
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._post(self.rest_users + "/" + str(id) + "/status/reactivate", '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def reactivate_user_by_name(self, username=None):
        """Will reactivate an user.

        :param username: The username of the user to reactivate.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.reactivate_user_by_name("rossini")
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')

        data = self._post(self.rest_users + "/reactivateByUsername/" + username, '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def suspend_user_by_id(self, id=None):
        """Will suspend an user.

        :param id: The id of the user to suspend.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.suspend_user_by_id(1)
        {u'status': u'suspended', u'username': u'rossini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._post(self.rest_users + "/" + str(id) + "/status/suspend", '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def suspend_user_by_name(self, username=None):
        """Will suspend an user.

        :param username: The username of the user to suspend.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.suspend_user_by_("rossini")
        {u'status': u'suspended', u'username': u'rossini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')

        data = self._post(self.rest_users + "/suspendByUsername/" + username, '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_user_by_id(self, id=None):
        """Will delete an user.

        :param id: The id of the user to delete.
        :type id: int
        :return: True when user is deleted, False when user don't exists or something failed.
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get("/syncope/rest/user/delete/" + str(id))

        if data.status_code == 200:
            return True
        else:
            return False

    def get_roles(self):
        """Get information from all roles in JSON.

        :return: False when something went wrong, or json data with all information from all roles.
        """
        data = self._get(self.rest_roles)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_role_by_id(self, id=None):
        """Will get all data from specific role, specified via id.

        :param id: The id of the role to get information.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific role.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_role_by_id(2)
        {u'inheritVirtualAttributes': False, u'inheritDerivedAttributes': False, u'roleOwner': None, u'name': u'child', u'parent': 1, <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get(self.rest_roles + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_parent_role_by_id(self, id=None):
        """Will get all data for the parent of the provided role id.

        :param id: The id of the role to get the parent information.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific role.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_parent_role_by_id(2)
        {u'inheritVirtualAttributes': False, u'inheritDerivedAttributes': False, u'roleOwner': None, u'name': u'root', u'parent': 0, <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get(self.rest_roles + "/" + str(id) + "/parent")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_children_role_by_id(self, id=None):
        """Will get all data for the parent of the provided role id.

        :param id: The id of the role to get the parent information.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific role.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_children_role_by_id(4)
        [{u'inheritVirtualAttributes': False, u'inheritDerivedAttributes': False, u'roleOwner': None, u'name': u'secretary', u'parent': 4, <cut>}]
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get(self.rest_roles + "/" + str(id) + "/children")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_role(self, arguments=None):
        """Will create an role.

        :param arguments: An JSON structure for creating the role. An example can be found in the 'examples' folder.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the just created role.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> create_role = '{"attributes":[{"schema":"icon","values":[],"readonly":false},{"schema":"rderived_dx","values":[],"readonly":false},{"schema":"rderived_sx","values":[],"readonly":false},{"schema":"show","values":["false"],"readonly":false},{"schema":"title","values":["My new attribute Title."],"readonly":false}],"id":0,"derivedAttributes":[],"virtualAttributes":[],"resources":["ws-target-resource-2","ws-target-resource-1"],"propagationStatusTOs":[],"name":"my_new_role","parent":1,"userOwner":null,"roleOwner":null,"inheritOwner":true,"inheritAttributes":false,"inheritDerivedAttributes":false,"inheritVirtualAttributes":false,"inheritPasswordPolicy":false,"inheritAccountPolicy":false,"entitlements":["CONFIGURATION_CREATE","CONFIGURATION_DELETE"],"passwordPolicy":4,"accountPolicy":6}'
        >>> print syn.create_role(create_role)
        {u'inheritVirtualAttributes': False, u'inheritDerivedAttributes': False, u'roleOwner': None, u'name': u'my_new_role', u'parent': 1, <cut>}
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        data = self._post(self.rest_roles, arguments)

        if data.status_code == 201:
            return data.json()
        else:
            return False

    def delete_role_by_id(self, id=None):
        """Will delete an role.

        :param id: The id of the role to delete.
        :type id: int
        :return: True when role is deleted, False when role don't exists or something failed.
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get("/syncope/rest/role/delete/" + str(id))

        if data.status_code == 200:
            return True
        else:
            return False

    def update_role(self, arguments=None):
        """Will update an role.

        :param arguments: An JSON structure for updating the role.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the just updated role.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_role = '{"id":102,"attributesToBeUpdated":[{"schema":"title","valuesToBeAdded":["My next new attribute Title."],"valuesToBeRemoved":["My new attribute Title."]}],"attributesToBeRemoved":["icon","rderived_sx","title","rderived_dx"],"derivedAttributesToBeAdded":[],"derivedAttributesToBeRemoved":[],"virtualAttributesToBeUpdated":[{"schema":"rvirtualdata","valuesToBeAdded":["virtual"],"valuesToBeRemoved":[]}],"virtualAttributesToBeRemoved":[],"resourcesToBeAdded":[],"resourcesToBeRemoved":["ws-target-resource-2"],"name":null,"userOwner":{"id":null},"roleOwner":{"id":null},"inheritOwner":true,"inheritAttributes":false,"inheritDerivedAttributes":false,"inheritVirtualAttributes":false,"inheritAccountPolicy":false,"inheritPasswordPolicy":false,"entitlements":["CONFIGURATION_CREATE","CONFIGURATION_DELETE","CONNECTOR_DELETE"],"passwordPolicy":{"id":4},"accountPolicy":{"id":6}}'
        >>> print syn.update_role(update_role)
        {u'inheritVirtualAttributes': False, u'inheritDerivedAttributes': False, u'roleOwner': None, u'name': u'my_new_role', u'parent': 1, <cut>}
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        data = self._post("/syncope/rest/role/update", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_log_levels(self):
        """Get information from all log levels in JSON.

        :return: False when something went wrong, or json data with all information from all log levels.
        """
        data = self._get(self.rest_logging)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_log_level_by_name(self, name=None):
        """Get information for specific log level.

        :param name: The name of the log level.
        :type name: String
        :return: False when something went wrong, or json data with information of the log level.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_log_level_by_name("ROOT")
        {u'name': u'ROOT', u'level': u'OFF'}
        """
        if name is None:
            raise ValueError('This search needs log level name to work!')
        data = self._get(self.rest_logging + "/" + name)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_or_update_log_level(self, arguments=None):
        """Will create or update an log level.

        :param arguments: An JSON structure for creating or updating the log level.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the just updated log level.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_loglevel = '{"name": "ROOT", "level": "INFO"}'
        >>> print syn.create_or_update_log_level(update_loglevel)
        {u'name': u'ROOT', u'level': u'INFO'}
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        json_data = json.loads(arguments)
        if json_data:
            log_name = json_data['name']
            log_level = json_data['level']
        else:
            return False

        data = self._post("syncope/rest/logger/log/" + log_name + "/" + log_level, arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_log_level_by_name(self, name=None):
        """Will delete an log level by the name.

        :param name: The name of the log level.
        :type name: String
        :return: False when something went wrong, or True when log level is deleted successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.delete_log_level_by_name("SYNCOPE")
        True
        """
        if name is None:
            raise ValueError('This search needs log level name to work!')
        data = self._delete(self.rest_logging + "/" + name)

        if data.status_code == 204:
            return True
        else:
            return False

    def get_audit(self):
        """Get information from all audit rules in JSON.

        :return: False when something went wrong, or json data with information from all audit rule.
        """
        data = self._get(self.rest_log_audit)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_audit(self, arguments=None):
        """Will create an log level.

        :param arguments: An JSON structure for creating the audit rule.
        :type arguments: JSON
        :return: False when something went wrong, or True when audit rule is created.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> add_audit_rule = '{"type":"REST","category":"LoggerController","subcategory":null,"event":"listAudits","result":"SUCCESS"}'
        >>> print syn.create_audit(add_audit_rule)
        True
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        data = self._put("syncope/rest/logger/audit/enable", arguments)

        if data.status_code == 200:
            return True
        else:
            return False

    def delete_audit(self, arguments=None):
        """Will delete an audit rule.

        :param arguments: An JSON structure for deleting the audit rule.
        :type arguments: JSON
        :return: False when something went wrong, True when delete of audit rule is successful.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> delete_audit_rule = '{"type":"REST","category":"LoggerController","subcategory":null,"event":"listAudits","result":"SUCCESS"}'
        >>> print syn.delete_audit(delete_audit_rule)
        True
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        data = self._put("syncope/rest/logger/audit/disable", arguments)

        if data.status_code == 200:
            return True
        else:
            return False

    def get_configurations(self):
        """Will get all configured configuration options.

        :return: False when something went wrong, or json data with all information from all configurations.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_configurations()
        [{u'value': u'SHA1', u'key': u'password.cipher.algorithm'}, {u'value': u'not-existing', <cut>
        """
        data = self._get(self.rest_configurations)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_configuration_by_key(self, key=None):
        """Will get the info for specific configuration key.

        :param key: The "key" name of the configuration item.
        :type key: String
        :return: False when something went wrong, or json data with all information from the configuration.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_configuration_by_key("password.cipher.algorithm")
        {u'value': u'SHA1', u'key': u'password.cipher.algorithm'}
        """
        if key is None:
            raise ValueError('This search needs an configuration key to work!')
        data = self._get(self.rest_configurations + "/" + key)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_configuration(self, arguments=None):
        """Will create an configuration item.

        :param arguments: An JSON structure for creating the configuration.
        :type arguments: JSON
        :return: False when something went wrong, or True when configuration is created.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> add_configuration = '{"value": true, "key": "we.all.love.pizza"}'
        >>> print syn.create_configuration(add_configuration)
        True
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        data = self._post(self.rest_configurations, arguments)

        if data.status_code == 201:
            return True
        else:
            return False

    def update_configuration(self, arguments=None):
        """Will update the configuration.

        :param arguments: An JSON structure for updating the configuration.
        :type arguments: JSON
        :return: False when something went wrong, or True when the configuration is updated.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_configuration = '{"value": false, "key": "we.all.love.pizza"}'
        >>> print syn.update_configuration(update_configuration)
        True
        """
        if arguments is None:
            raise ValueError('This search needs JSON data to work!')

        json_data = json.loads(arguments)
        if "key" in json_data:
            config_key = json_data['key']
        else:
            return False

        data = self._put(self.rest_configurations + "/" + config_key, arguments)

        if data.status_code == 204:
            return True
        else:
            return False

    def delete_configuration_by_key(self, key=None):
        """Will delete an configuration item..

        :param key: The "key" name of the configuration item.
        :type key: JSON
        :return: False when something went wrong, or True when configuration is deleted.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.delete_configuration_by_key("we.all.love.pizza")
        True
        """
        if key is None:
            raise ValueError('This search needs JSON data to work!')

        data = self._delete(self.rest_configurations + "/" + key)

        if data.status_code == 204:
            return True
        else:
            return False

    def get_configuration_validators(self):
        """Will get the info for the configuration validators.

        :return: False when something went wrong, or json data with all information from the validators.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_configuration_validators()
        [{u'name': u'org.apache.syncope.core.persistence.validation.attrvalue.AlwaysTrueValidator'}, <cut>
        """
        data = self._get(self.rest_configurations + "/validators")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_configuration_mailtemplates(self):
        """Will get the info for the mailtemplates.

        :return: False when something went wrong, or json data with all information about the mailtemplates.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_configuration_mailtemplates()
        [{u'name': u'optin'}]
        """
        data = self._get(self.rest_configurations + "/mailTemplates")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_configuration_stream(self):
        """Returns configuration as an downloadable content.xml database export file.

        :return: False when something went wrong, or XML data.

        >>> import xml.etree.ElementTree as ET
        >>> import syncope

        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> response = syn.get_configuration_stream()
        >>> tree = ET.parse(response.text)
        >>> root = tree.getroot()
        >>> print tree
        """
        data = self._get_xml(self.rest_configurations + "/stream")

        if data.status_code == 200:
            return data
        else:
            return False

    def get_entitlements(self):
        """Will return a list of all known entitlements.

        :return: False when something went wrong, or json data with all know entitlements.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_entitlements()
        [{u'name': u'NOTIFICATION_UPDATE'}, {u'name': u'SCHEMA_CREATE'}, <cut>
        """
        data = self._get(self.rest_entitlements)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_own_entitlements(self):
        """Will return a list of all known entitlements.

        :return: False when something went wrong, or json data with all know entitlements.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_own_entitlements()
        [{u'name': u'NOTIFICATION_UPDATE'}, {u'name': u'SCHEMA_CREATE'}, <cut>
        """
        data = self._get(self.rest_entitlements + "/own")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_notifications(self):
        """Will return a list of all notifications.

        :return: False when something went wrong, or json data with all notifications.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_notifications()
        [{u'recipientAttrType': u'UserSchema', u'about': {u'membershipCond': None, <cut>
        """
        data = self._get(self.rest_notifications)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_notification_by_id(self, id=None):
        """Will return information for notification by id.

        :param id: The notification ID.
        :type id: Int.
        :return: False when something went wrong, or json data with all notifications.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_notification_by_id(1)
        [{u'recipientAttrType': u'UserSchema', u'about': {u'membershipCond': None, <cut>
        """
        if id is None:
            raise ValueError('This search needs an id to work!')
        data = self._get(self.rest_notifications + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_notification(self, arguments=None):
        """Get create an notification.

        :param arguments: An JSON structure for creating the notification.
        :type arguments: JSON
        :return: False when something went wrong, or True when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> create_notification = '{"events":["[REST]:[LoggerController]:[]:[deleteLog]:[SUCCESS]","[REST]:[LoggerController]:[]:[disableAudit]:[SUCCESS]"],"recipientAttrType":"Username","recipientAttrName":"Username","selfAsRecipient":true,"sender":"me@home.nl","subject":"this is something very important","template":"optin","traceLevel":"FAILURES"}'
        >>> print syn.create_notification(create_notification)
        True
        """
        if arguments is None:
            raise ValueError('This search needs an JSON to work!')
        data = self._post(self.rest_notifications, arguments)

        if data.status_code == 201:
            return True
        else:
            return False

    def update_notification_by_id(self, arguments=None):
        """Get information for specific log level.

        :param arguments: An JSON structure for updating the notification.
        :type arguments: JSON
        :return: False when something went wrong, or True when updated successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_notification = '{"id":104,"events":["[REST]:[LoggerController]:[]:[deleteLog]:[SUCCESS]"],"about":null,"recipients":null,"recipientAttrType":"Username","recipientAttrName":"Username","selfAsRecipient":true,"sender":"me@home.nl","subject":"this is something very important","template":"optin","traceLevel":"FAILURES"}'
        >>> print syn.update_notification_by_id(update_notification)
        True
        """
        if arguments is None:
            raise ValueError('This search needs an JSON to work!')
        data = self._post("syncope/rest/notification/update", arguments)

        if data.status_code == 200:
            return True
        else:
            return False

    def delete_notification_by_id(self, id=None):
        """Get information for specific log level.

        :param name: The id for the notification.
        :type name: Int
        :return: False when something went wrong, or True when deleted successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.delete_notification_by_id(104)
        True
        """
        if id is None:
            raise ValueError('This search needs an JSON to work!')
        data = self._delete(self.rest_notifications + "/" + str(id))

        if data.status_code == 204:
            return True
        else:
            return False

    def get_account_policies(self):
        """Will return a list of account policies.

        :return: False when something went wrong, or json data with all account policies.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_account_policies()
        [{u'usedByResources': [], u'description': u'sample account policy', <cut>
        """
        data = self._get(self.cxf_account_policies)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_account_policy_by_id(self, id=None):
        """Will return information with account policy for id.

        :return: False when something went wrong, or json data with information for account policie.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_account_policy_by_id(5)
        {u'usedByResources': [u'ws-target-resource-1', u'ws-target-resource-2', u'ws-target-resource-timeout', <cut>
        """
        if id is None:
            raise ValueError('This needs an ID to work!')
        data = self._get(self.cxf_account_policies + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_account_policy(self, arguments=None):
        """Will create an account policy.

        :param arguments: An JSON structure for creating the account policy.
        :type arguments: JSON
        :return: False when something went wrong, or JSON data when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> create_account_policy = '{"description":"My Description","type":"ACCOUNT","usedByResources":[],"usedByRoles":[],"specification":{"maxLength":0,"minLength":0,"pattern":null,"wordsNotPermitted":[],"schemasNotPermitted":["firstname","email"],"prefixesNotPermitted":[],"suffixesNotPermitted":[],"allUpperCase":false,"allLowerCase":false,"propagateSuspension":false,"permittedLoginRetries":0}}'
        >>> print syn.create_account_policy(create_account_policy)
        {u'usedByResources': [], u'description': u'My Description', u'specification': { <cut>
        """
        if arguments is None:
            raise ValueError('This create needs an JSON to work!')
        data = self._post(self.rest_account_policies + "/create", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def update_account_policy(self, arguments=None):
        """Will update an account policy.

        :param arguments: An JSON structure for updating the account policy.
        :type arguments: JSON
        :return: False when something went wrong, or JSON data when updated successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_account_policy = '{"id":1001,"description":"My Description 2","type":"ACCOUNT","usedByResources":[],"usedByRoles":[],"specification":{"maxLength":0,"minLength":0,"pattern":null,"wordsNotPermitted":[],"schemasNotPermitted":["firstname"],"prefixesNotPermitted":[],"suffixesNotPermitted":[],"allUpperCase":false,"allLowerCase":false,"propagateSuspension":false,"permittedLoginRetries":0}}'
        >>> print syn.create_account_policy(update_account_policy)
        {u'usedByResources': [], u'description': u'My Description', u'specification': { <cut>
        """
        if arguments is None:
            raise ValueError('This update needs an JSON to work!')
        data = self._post(self.rest_account_policies + "/update", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_account_policy(self, id=None):
        """Will delete an account policy.

        :param id: The account policy id.
        :type id: Int
        :return: False when something went wrong, or True when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.delete_account_policy(1001)
        True
        """
        if id is None:
            raise ValueError('This delete needs an id to work!')
        data = self._delete(self.cxf_account_policies + "/" + str(id))

        if data.status_code == 204:
            return True
        else:
            return False

    def get_sync_policies(self):
        """Will return a list of sync policies.

        :return: False when something went wrong, or json data with all sync policies.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_account_policies()
        [{u'usedByResources': [u'resource-csv'], u'description': u'sync policy 2' <cut>
        """
        data = self._get(self.cxf_sync_policies)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_sync_policy_by_id(self, id=None):
        """Will return information with sync policy for id.

        :return: False when something went wrong, or json data with information for sync policy.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_sync_policy_by_id(9)
        {u'usedByResources': [u'ws-target-resource-2'], u'description': u'sync policy for java rule', <cut>
        """
        if id is None:
            raise ValueError('This needs an ID to work!')
        data = self._get(self.cxf_account_policies + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_sync_policy(self, arguments=None):
        """Will create an sync policy.

        :param arguments: An JSON structure for creating the sync policy.
        :type arguments: JSON
        :return: False when something went wrong, or JSON data when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> create_sync_policy = '{"description":"My First Sync","type":"SYNC","usedByResources":[],"usedByRoles":[],"specification":{"uAltSearchSchemas":["loginDate"],"userJavaRule":null,"rAltSearchSchemas":[],"roleJavaRule":null,"conflictResolutionAction":"FIRSTMATCH"}}'
        >>> print syn.create_sync_policy(create_sync_policy)
        {u'usedByResources': [], u'description': u'My Description', u'specification': { <cut>
        """
        if arguments is None:
            raise ValueError('This create needs an JSON to work!')
        data = self._post(self.rest_sync_policies + "/create", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def update_sync_policy(self, arguments=None):
        """Will update an sync policy.

        :param arguments: An JSON structure for updating the account policy.
        :type arguments: JSON
        :return: False when something went wrong, or JSON data when updated successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_sync_policy = '{"id":1001, "description":"My First Sync","type":"SYNC","usedByResources":[],"usedByRoles":[],"specification":{"uAltSearchSchemas":["loginDate"],"userJavaRule":null,"rAltSearchSchemas":[],"roleJavaRule":null,"conflictResolutionAction":"FIRSTMATCH"}}'
        >>> print syn.create_sync_policy(update_sync_policy)
        {u'usedByResources': [], u'description': u'My Description', u'specification': { <cut>
        """
        if arguments is None:
            raise ValueError('This update needs an JSON to work!')
        data = self._post(self.rest_sync_policies + "/update", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_sync_policy(self, id=None):
        """Will delete an account policy.

        :param id: The account policy id.
        :type id: Int
        :return: False when something went wrong, or True when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.delete_sync_policy(1001)
        True
        """
        if id is None:
            raise ValueError('This delete needs an id to work!')
        data = self._delete(self.cxf_sync_policies + "/" + str(id))

        if data.status_code == 204:
            return True
        else:
            return False

    def get_password_policies(self):
        """Will return a list of password policies.

        :return: False when something went wrong, or json data with all password policies.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_account_policies()
        [{u'usedByResources': [u'resource-csv'], u'description': u'password policy 2' <cut>
        """
        data = self._get(self.cxf_password_policies)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_password_policy_by_id(self, id=None):
        """Will return information with password policy for id.

        :return: False when something went wrong, or json data with information for password policy.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_password_policy_by_id(9)
        {u'usedByResources': [u'ws-target-resource-2'], u'description': u'password policy for java rule', <cut>
        """
        if id is None:
            raise ValueError('This needs an ID to work!')
        data = self._get(self.cxf_account_policies + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def create_password_policy(self, arguments=None):
        """Will create an password policy.

        :param arguments: An JSON structure for creating the password policy.
        :type arguments: JSON
        :return: False when something went wrong, or JSON data when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> create_password_policy = '{"description":"My First Sync","type":"SYNC","usedByResources":[],"usedByRoles":[],"specification":{"uAltSearchSchemas":["loginDate"],"userJavaRule":null,"rAltSearchSchemas":[],"roleJavaRule":null,"conflictResolutionAction":"FIRSTMATCH"}}'
        >>> print syn.create_password_policy(create_password_policy)
        {u'usedByResources': [], u'description': u'My Description', u'specification': { <cut>
        """
        if arguments is None:
            raise ValueError('This create needs an JSON to work!')
        data = self._post(self.rest_password_policies + "/create", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def update_password_policy(self, arguments=None):
        """Will update an password policy.

        :param arguments: An JSON structure for updating the account policy.
        :type arguments: JSON
        :return: False when something went wrong, or JSON data when updated successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> update_password_policy = '{"id":1001, "description":"My First Sync","type":"SYNC","usedByResources":[],"usedByRoles":[],"specification":{"uAltSearchSchemas":["loginDate"],"userJavaRule":null,"rAltSearchSchemas":[],"roleJavaRule":null,"conflictResolutionAction":"FIRSTMATCH"}}'
        >>> print syn.create_password_policy(update_password_policy)
        {u'usedByResources': [], u'description': u'My Description', u'specification': { <cut>
        """
        if arguments is None:
            raise ValueError('This update needs an JSON to work!')
        data = self._post(self.rest_password_policies + "/update", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_password_policy(self, id=None):
        """Will delete an account policy.

        :param id: The account policy id.
        :type id: Int
        :return: False when something went wrong, or True when created successfully.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.delete_password_policy(1001)
        True
        """
        if id is None:
            raise ValueError('This delete needs an id to work!')
        data = self._delete(self.cxf_password_policies + "/" + str(id))

        if data.status_code == 204:
            return True
        else:
            return False


    # def get_resources(self):
    #     """Will search an user and will return the data by pages.
    #
    #     :return: False when something went wrong, or json data with all information from all resources.
    #     :Example:
    #
    #     >>> import syncope
    #     >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    #     >>> print syn.get_resources()
    #     [{u'rmapping': None, u'randomPwdIfNotProvided': False, u'propagationPrimary': True, u'enforceMandatoryCondition': False <cut>
    #     """
    #     data = self._get(self.rest_resources)
    #
    #     if data.status_code == 200:
    #         return data.json()
    #     else:
    #         return False
    #
    # def create_resource(self, arguments=None):
    #     """Will search an user and will return the data by pages.
    #
    #     :return: False when something went wrong, or json data with all information from all resources.
    #     :Example:
    #
    #     >>> import syncope
    #     >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    #     >>> print syn.get_resources()
    #     [{u'rmapping': None, u'randomPwdIfNotProvided': False, u'propagationPrimary': True, u'enforceMandatoryCondition': False <cut>
    #     """
    #     data = self._post(self.rest_resources, arguments)
    #
    #     if data.status_code == 200:
    #         return data.json()
    #     else:
    #         return False
    #
    # def create_connector(self, arguments=None):
    #     """Will search an user and will return the data by pages.
    #
    #     :return: False when something went wrong, or json data with all information from all resources.
    #     :Example:
    #
    #     >>> import syncope
    #     >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    #     >>> print syn.get_resources()
    #     [{u'rmapping': None, u'randomPwdIfNotProvided': False, u'propagationPrimary': True, u'enforceMandatoryCondition': False <cut>
    #     """
    #     data = self._post(self.rest_connectors, arguments)
    #
    #     if data.status_code == 200:
    #         return data.json()
    #     else:
    #         return False
