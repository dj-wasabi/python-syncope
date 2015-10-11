"""python-syncope is an python wrapper for the Syncope Rest API."""


__author__ = 'Werner Dijkerman'
__version__ = '0.0.2'
__license__ = "Apache License 2.0"
__email__ = "ikben@werner-dijkerman.nl"

import requests


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

        return requests.post(syncope_path, auth=(self.username, self.password), headers=self.headers, data=arguments, timeout=self.timeout)

    def create_users(self, arguments):
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

    def get_users(self):
        """Get information from all users in JSON.

        :return: False when something went wrong, or json data with all information from all users.
        """
        data = self._get(self.rest_users)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_id(self, id=None):
        """Will get all data from specific user, specified via id.

        :param id: The id of the user to get information.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_users_id(5)
        {u'status': u'active', u'username': u'puccini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._get(self.rest_users + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_search(self, arguments=None):
        """Will search an user. It will require an python dict to be used for the searching.

        :param arguments: An JSON structure. See example for more information.
        :type arguments: JSON
        :return: False when something went wrong, or json data with all information from the search request.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
        >>> print syn.get_users_search(search_req)
        {u'status': u'active', u'username': u'vivaldi', <cut>}
        >>> search_req = '{"type":"LEAF","resourceCond":{"resourceName":"ws-target-resource-1"}}'
        >>> print syn.get_users_search(search_req)
        {u'status': u'active', u'username': u'vivaldi', <cut>}
        """
        if arguments is None:
            raise ValueError('This search needs an dict to work!')

        data = self._post(self.rest_users +"/search", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_search_count(self, arguments=None):
        """Will count the users matching the search request.

        :param arguments: An JSON structure. See example for more information.
        :type arguments: JSON
        :return: False when something went wrong, or the amount of users matching the request.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> search_req = '{"type":"LEAF","attributableCond":{"type":"EQ","schema":"username","expression":"vivaldi"}}'
        >>> print syn.get_users_search_count(search_req)
        5
        >>> search_req = '{"type":"LEAF","resourceCond":{"resourceName":"ws-target-resource-1"}}'
        >>> print syn.get_users_search_count(search_req)
        1
        """
        if arguments is None:
            raise ValueError('This search needs an dict to work!')

        data = self._post(self.rest_users +"/search/count", arguments)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_search_page(self, arguments=None, page=None, size=None):
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
        >>> print syn.get_users_search_page(search_user, 1, 1)
        {u'status': u'active', u'username': u'rossini', <cut>}
        >>> print syn.get_users_search_page(search_user, 3, 1)
        {u'status': u'active', u'username': u'vivaldi', <cut>}
        """
        if arguments is None:
            raise ValueError('This search needs an dict to work!')
        if page is None:
            raise ValueError('This search needs an page to work!')
        if size is None:
            raise ValueError('This search needs an size to work!')

        data = self._post(self.rest_users +"/search", arguments, "?page=" + str(page) + "&size=" + str(size))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_username(self, username=None):
        """Will get all data from specific user, specified via username.

        :param username: The username of the user to get information.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.get_users_username("puccini")
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

    def edit_users_id_activate(self, id=None):
        """Will activate an user.

        :param id: The id of the user to activate.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.edit_users_id_activate(1)
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._post(self.rest_users + "/" + str(id) + "/status/activate", '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_username_activate(self, username=None):
        """Will activate an user.

        :param username: The username of the user to activate.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.edit_users_username_activate("rossini")
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')

        data = self._post(self.rest_users + "/activateByUsername/" + username, '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_id_reactivate(self, id=None):
        """Will reactivate an user.

        :param id: The id of the user to reactivate.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.edit_users_id_reactivate(1)
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._post(self.rest_users + "/" + str(id) + "/status/reactivate", '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_username_reactivate(self, username=None):
        """Will reactivate an user.

        :param username: The username of the user to reactivate.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.edit_users_username_reactivate("rossini")
        {u'status': u'active', u'username': u'rossini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')

        data = self._post(self.rest_users + "/reactivateByUsername/" + username, '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_id_suspend(self, id=None):
        """Will suspend an user.

        :param id: The id of the user to suspend.
        :type id: int
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.edit_users_id_suspend(1)
        {u'status': u'suspended', u'username': u'rossini', <cut>}
        """
        if id is None:
            raise ValueError('This search needs an id to work!')

        data = self._post(self.rest_users + "/" + str(id) + "/status/suspend", '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_username_suspend(self, username=None):
        """Will suspend an user.

        :param username: The username of the user to suspend.
        :type username: string
        :return: False when something went wrong, or json data with all information from this specific user.
        :Example:

        >>> import syncope
        >>> syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
        >>> print syn.edit_users_username_suspend("rossini")
        {u'status': u'suspended', u'username': u'rossini', <cut>}
        """
        if username is None:
            raise ValueError('This search needs an username to work!')

        data = self._post(self.rest_users + "/suspendByUsername/" + username, '{}')
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_users_id(self, id=None):
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
