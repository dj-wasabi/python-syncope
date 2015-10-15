Test Results
============

Overview of the test results from the latest working version. Also the Test coverage is shown:

.. code-block:: bash

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
    tests/test_syncope.py::test_get_role_by_id PASSED
    ------------------------------------------------------ coverage: platform darwin, python 2.7.10-final-0 -------------------------------------------------------
    Name                  Stmts   Miss  Cover   Missing
    ---------------------------------------------------
    syncope/__init__.py     155     42    73%

    ================================================================== 21 passed in 2.04 seconds ==================================================================
