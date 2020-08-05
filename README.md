# last_on
Hi! this is a finished API that takes module- employer that has 5 attributes (name, ID, phone, email, contacts)
contacts attribute is a module as well that has 4 attributes(name, last name, email, phone) 
both are stored in DB
both modules you can Create, Read, Update, Delete, get as .JSON (on GET button on the top right side of the API)
you are able to download an EXCEL file for the employer DB by adding (/xls/) to the root url
you can enter a year and a month number and receive the numbers of days that month has by writing (/lastday/<int:year>/<int:month>) in the root url
  *must install
  pip install djangorestframework
  pip install xlwt
  pip install calender
  in order to use MYSQL and be sure you have MySQL python connector
  pip instell mysqlclient
  create a new DB and grat a user all privileges 
  and modify the settings.py deefult DB to 
  1)ALLOWED_HOSTS = ['your server IP address']
  2)DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<DB_name>',
        'USER': '<user_granted_all_privileges>',
        'PASSWORD': '<>pass_set_for_user',
        'HOST': 'localhost',
        'PORT': '3306',
       } 
    }
3) python manage.py migrate

and thats it thank you

fell free to ask questions!!


