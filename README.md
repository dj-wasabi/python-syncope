Work in progress
=========

####Table of Contents
1. [Overview](#overview)
2. [Requirements](#requirements)
3. [Syncope Version](#syncope-versions)
4. [Installing this role](#installation)
5. [Some Examples](#small-example)
6. [Documentation](#documentation)
7. [License](#license)
8. [Author Information](#author-information)

#Overview

python-syncope is an python wrapper around the Syncope Rest API.
At the moment, only some user specific actions can be executed against an Syncope instance. Also basic python tests are missing and not all documentation is created.

#Requirements

* requests

#Syncope Versions

At the moment, the python-syncope will only work on the Syncope 1.1.x releases. Goal is that it will support 1.2 too.

#Installation

    pip install python-syncope


#Small example

How to use syncope:

    import syncope
    syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")
    
    print syn.edit_users_username_suspend("puccini")
    print syn.edit_users_username_reactivate("puccini")
    print syn.edit_users_username_reactivate("puccini")
Output:

    {u'status': u'suspended', u'username': u'puccini', u'creationDate': 1287572400000, u'derivedAttributes': [], u'failedLogins': 0, u'tokenExpireTime': None, u'memberships': [{u'derivedAttributes': [], u'roleName': u'artDirector', u'virtualAttributes': [], u'resources': [], u'roleId': 14, u'attributes': [], u'id': 7, u'propagationStatusTOs': []}], u'token': None, u'virtualAttributes': [], u'resources': [], u'lastLoginDate': None, u'changePwdDate': None, u'attributes': [{u'readonly': False, u'values': [u'Giacomo'], u'schema': u'firstname'}, {u'readonly': False, u'values': [u'Puccini'], u'schema': u'surname'}, {u'readonly': False, u'values': [u'Giacomo Puccini'], u'schema': u'fullname'}, {u'readonly': False, u'values': [u'puccini@apache.org'], u'schema': u'userId'}], u'password': u'5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8', u'id': 5, u'propagationStatusTOs': []}
    {u'status': u'active', u'username': u'puccini', u'creationDate': 1287572400000, u'derivedAttributes': [], u'failedLogins': 0, u'tokenExpireTime': None, u'memberships': [{u'derivedAttributes': [], u'roleName': u'artDirector', u'virtualAttributes': [], u'resources': [], u'roleId': 14, u'attributes': [], u'id': 7, u'propagationStatusTOs': []}], u'token': None, u'virtualAttributes': [], u'resources': [], u'lastLoginDate': None, u'changePwdDate': None, u'attributes': [{u'readonly': False, u'values': [u'Giacomo'], u'schema': u'firstname'}, {u'readonly': False, u'values': [u'Puccini'], u'schema': u'surname'}, {u'readonly': False, u'values': [u'Giacomo Puccini'], u'schema': u'fullname'}, {u'readonly': False, u'values': [u'puccini@apache.org'], u'schema': u'userId'}], u'password': u'5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8', u'id': 5, u'propagationStatusTOs': []}
    False

#Documentation

Will be available soon on readthedocs.org

#License

python-syncope is licensed under the Apache License 2.0. Check the LICENSE file.

#Author Information

