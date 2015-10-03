"""python-syncope is an python wrapper for the Syncope Rest API."""


__author__ = 'Werner Dijkerman'
__version__ = '0.0.1'
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
        syncope_path = "{0}/{1}".format(self.syncope_url, rest_path)
        print syncope_path

        return requests.delete(syncope_path, auth=(self.username, self.password), headers=self.headers, timeout=self.timeout)

    def _post(self, rest_path, arguments=None):
        """Will do an POST action for creating or to update the information from the syncope server. This function will be called from the actual actions.

        :param rest_path: uri of the rest action.
        :param arguments: Optional arguments.
        :return: Returns the data in json (if any)from the POST request.
        """
        if arguments is not None:
            syncope_path = "{0}/{1}.json{2}".format(self.syncope_url, rest_path, arguments)
        else:
            syncope_path = "{0}/{1}.json".format(self.syncope_url, rest_path)

        return requests.post(syncope_path, auth=(self.username, self.password), headers=self.headers, data=arguments, timeout=self.timeout)

    def get_users(self):
        """Get information from all users in JSON.

        :return: False when something went wrong, or json data with all information from all users.
        """
        data = self._get(self.rest_users)

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_id(self, id):
        """Will get all data from specific user, specified via id.

        :param id: The id of the user to get information.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._get(self.rest_users + "/" + str(id))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_name(self, username):
        """Will get all data from specific user, specified via username.

        :param username: The username of the user to get information.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._get(self.rest_users, "?username=" + str(username))

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def get_users_count(self):
        """Will count all users found in Syncope.

        :return: False when something went wrong, or the amount of users.
        """
        data = self._get(self.rest_users + "/count")

        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_id_activate(self, id):
        """Will activate an user.

        :param id: The id of the user to activate.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._post(self.rest_users + "/" + str(id) + "/status/activate")
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_username_activate(self, username):
        """Will activate an user.

        :param username: The username of the user to activate.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._post(self.rest_users + "/activateByUsername/" + username)
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_id_reactivate(self, id):
        """Will reactivate an user.

        :param id: The id of the user to reactivate.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._post(self.rest_users + "/" + str(id) + "/status/reactivate")
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_username_reactivate(self, username):
        """Will reactivate an user.

        :param username: The username of the user to reactivate.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._post(self.rest_users + "/reactivateByUsername/" + username)
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_id_suspend(self, id):
        """Will suspend an user.

        :param id: The id of the user to suspend.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._post(self.rest_users + "/" + str(id) + "/status/suspend")
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def edit_users_username_suspend(self, username):
        """Will suspend an user.

        :param username: The username of the user to suspend.
        :return: False when something went wrong, or json data with all information from this specific user.
        """
        data = self._post(self.rest_users + "/suspendByUsername/" + username)
        if data.status_code == 200:
            return data.json()
        else:
            return False

    def delete_users_id(self, id):
        """Will delete an user.

        :param id: The id of the user to delete.
        :return: True when user is deleted, False when user don't exists or something failed.
        """
        data = self._delete(self.rest_users + "/" + str(id))

        if data.status_code == 200:
            return True
        else:
            return False
