
**Django Phonebook**

Phonebook is a simple Django app to manage contacts (lastname, firstname, username, phone number, address) .
Application development and testing with django v4.2.4


Quick start
-----------

1. Set specific and custome settings for you project in ``local_settings.py``::

2. open terminal and  make migrations  for ``models`` ::

        python manage.py makemigrations     
        python manage.py migrate     

3.  ``extracting data and saving object`` by below instruction::

        python manage.py data_saver --start

4. Start the development and run``server`` ::

        python manage.py runserver

TODO
----

    - Create, edit, delete Locations data 
