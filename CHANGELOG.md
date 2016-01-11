#Changelog for python-syncope

Below an overview of all changes in the releases.

Version (Release date)

0.0.5   (2016-01-??)

  * Added configuration actions


0.0.4   (2015-10-25)

  * Added log levels actions.
  * Added audit rules.

0.0.3   (2015-10-20)

  * Renamed the functions:
    * create_users -> create_user
    * delete_users_id -> delete_user_by_id
    * edit_users_id_activate -> enable_user_by_id
    * edit_users_id_reactivate -> reactivate_user_by_id
    * edit_users_id_suspend -> suspend_user_by_id
    * edit_users_username_suspend -> suspend_user_by_name
    * edit_users_username_activate -> enable_user_by_name
    * edit_users_username_reactivate -> reactivate_user_by_name
    * get_users_id -> get_user_by_id
    * get_users_search -> get_users_by_query
    * get_users_search_page -> get_paged_users_by_query
    * get_users_search_count -> get_user_count_by_query
    * get_users_username -> get_user_by_name
  * Added code coverage into documentation.
  * Added roles related actions.

0.0.2   (2015-10-11)

  * Completed all "User" related actions.
  * Added examples folder with the first example: create_users.py
  * Added CHANGELOG.md
  * Added tests

0.0.1   (2015-10-03)

  * Initial small alpha version, with few functions for user related actions.
  * Can be found and installed with pip
