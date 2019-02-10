chuckwagon
==========

DC Food Truck Tracker

:License: MIT


Build Docker containers 
^^^^^^^^^^^^^^^^^^^^^^^
::
    $ docker-compose -f local.yml build 


Start server
^^^^^^^^^^^^
::
    $ docker-compose -f local.yml up

Navigate to localhost:8000/admin/


Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ docker-compose -f local.yml run --rm django coverage run -m pytest
    $ docker-compose -f local.yml run --rm django coverage html
    $ docker-compose -f local.yml run --rm django open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

  $ docker-compose -f local.yml run --rm django pytest
Running tests
~~~~~~~~~~~~~
::
  $ docker-compose -f local.yml run --rm django python manage.py test


