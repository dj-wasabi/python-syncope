#!/usr/bin/env python
#
# This example will update the user: wedijkerman (The one we created with the example script: create_user.py).
# We made an mistake with the username: We want to update the username from 'wedijkerman' to 'wdijkerman'.
#
import syncope

# Create the connection
syn = syncope.Syncope(syncope_url="http://192.168.10.13:9080", username="admin", password="password")

# Get the id for the 'wedijkerman' user, before we update it to 'wdijkerman'
my_user_data = syn.get_user_by_name("wedijkerman")
my_user_id = my_user_id['id']
my_user = '{"id": ' + str(my_user_id) + ',"username": "wdijkerman"}'

json_output = syn.update_users(my_user)

if json_output:
	print  "User %s created on this time %s" % (json_output['username'])
else:
	print "Create failed or user already exists."
