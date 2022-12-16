Wednesday
======

The basic employee management app using Python Flask



Installation steps
-------

Create a virtualenv and activate it::


    $ python -m venv env
    $ env\Scripts\activate

Install required packages from requirements.txt file using the following command::

    $ python -m pip install -r requirements.txt


Run the application using th following command::

   $ python setup.py


Open http://127.0.0.1:5000 in a browser.


Test
----
Total test cases - 5
::

    $ python -m pytest -p no:warnings tests/


Docker Instructions
----

::

To create and run a docker image execute::

  $ docker-compose up

and visit with your browser http://localhost:5000

Security Implementation
----

1. CSRF tokens are used.
2. werkzeug.Security is used for hashing the password to store in the DB.
3. Appropriate measure is taken to protect app from the SQL injection.
4. Major rights are given to admin only.

--> Loggin functionality is implemented.

Database
----

1. Sqlite Database is used.
2. To initialize the Database for the first time run the following code on the CLI.

    $ flask --app flaskApp init-db'

3. Separate Sqlite Database is used to store the data of the employee.
4. For API app a sync request is performed everytime the user data gets updated from the main app.



Main app functionality 
----
Total number of screens = 7 ( Login, register, about me, update, delete modals to delete the employee from the database, all_employee, search )

Admin access :- all screen available to the admin
1. Can delete and update all employee details including itself.
2. Can see all the information about all the employee in the organisation.
3. Can register a new employee at the backend.
4. Can change the employee role form admin to employee or vice versa.
5. Can change the admin status to employee in that case after successfull commit it will be logged out from the session.



Employee :- available screen(Login, register, aboutme, all_employee)
1. Can register itself in the registration page and then it will be redirected to the login page.
2. Can see all the employee in the orgnanization with only details name, cantact , emailid.
3. Can see about me page .
4. All other access are given to admin only.


restricted access to employee :-

1. Cannot delete or update any employee information in the database.
2. Can see only limited information about the employee.
3. Cannot change any employee role including itself.
