Tests
=====

Overview
--------

The following python versions are working:

+--------+-------------+-------------+
| python | Syncope 1.1 | Syncope 1.2 |
+========+=============+=============+
|  2.7   |     v       |      x      |
+--------+-------------+-------------+




Coverage
--------

Overview of the test results from the latest working version. Also the Test coverage is shown:

.. code-block:: bash

    plugins: cov-2.2.0
    collected 52 items

    tests/test_syncope.py::test___init__syncope_url PASSED
    tests/test_syncope.py::test___init__username PASSED
    tests/test_syncope.py::test___init__password PASSED
    tests/test_syncope.py::test__post PASSED
    tests/test_syncope.py::test_get_users_count PASSED
    tests/test_syncope.py::test_get_user_by_id PASSED
    tests/test_syncope.py::test_get_users_id_false PASSED
    tests/test_syncope.py::test_get_users_by_query PASSED
    tests/test_syncope.py::test_get_user_count_by_query PASSED
    tests/test_syncope.py::test_get_user_by_name PASSED
    tests/test_syncope.py::test_get_paged_users_by_query PASSED
    tests/test_syncope.py::test_suspend_user_by_id PASSED
    tests/test_syncope.py::test_reactivate_user_by_id PASSED
    tests/test_syncope.py::test_suspend_user_by_name PASSED
    tests/test_syncope.py::test_reactivate_user_by_name PASSED
    tests/test_syncope.py::test_create_user PASSED
    tests/test_syncope.py::test_update_user PASSED
    tests/test_syncope.py::test_delete_user_by_id PASSED
    tests/test_syncope.py::test_get_users PASSED
    tests/test_syncope.py::test_get_roles PASSED
    tests/test_syncope.py::test_get_roles_false PASSED
    tests/test_syncope.py::test_get_role_by_id PASSED
    tests/test_syncope.py::test_get_role_by_id_false PASSED
    tests/test_syncope.py::test_get_role_by_id_raise PASSED
    tests/test_syncope.py::test_get_parent_role_by_id PASSED
    tests/test_syncope.py::test_get_parent_role_by_id_false PASSED
    tests/test_syncope.py::test_get_parent_role_by_id_raise PASSED
    tests/test_syncope.py::test_get_children_role_by_id PASSED
    tests/test_syncope.py::test_get_children_role_by_id_false PASSED
    tests/test_syncope.py::test_get_children_role_by_id_raise PASSED
    tests/test_syncope.py::test_create_role PASSED
    tests/test_syncope.py::test_create_role_false PASSED
    tests/test_syncope.py::test_create_role_raise PASSED
    tests/test_syncope.py::test_update_role PASSED
    tests/test_syncope.py::test_update_role_false PASSED
    tests/test_syncope.py::test_update_role_railse PASSED
    tests/test_syncope.py::test_delete_role PASSED
    tests/test_syncope.py::test_delete_role_false PASSED
    tests/test_syncope.py::test_delete_role_raise PASSED
    tests/test_syncope.py::test_get_log_levels PASSED
    tests/test_syncope.py::test_get_log_levels_false PASSED
    tests/test_syncope.py::test_get_log_level_by_name PASSED
    tests/test_syncope.py::test_get_log_level_by_name_false PASSED
    tests/test_syncope.py::test_get_log_level_by_name_raise PASSED
    tests/test_syncope.py::test_create_or_update_log_level_update PASSED
    tests/test_syncope.py::test_create_or_update_log_level_create PASSED
    tests/test_syncope.py::test_create_or_update_log_level_false_empty PASSED
    tests/test_syncope.py::test_create_or_update_log_level_create_false PASSED
    tests/test_syncope.py::test_create_or_update_log_level_raise PASSED
    tests/test_syncope.py::test_delete_log_level_by_name PASSED
    tests/test_syncope.py::test_delete_log_level_by_name_false PASSED
    tests/test_syncope.py::test_delete_log_level_by_name_raise PASSED
    ------------------------------------------------------ coverage: platform darwin, python 2.7.10-final-0 -------------------------------------------------------
    Name                  Stmts   Miss  Cover   Missing
    ---------------------------------------------------
    syncope/__init__.py     190     39    79%
