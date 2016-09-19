from users import models
from getpass import getpass

print "Initializing database superuser..."
first_name = raw_input('First name: ')
last_name = raw_input('Last name: ')
password = getpass('pw: ')

person = models.Person(
    first_name=first_name,
    last_name=last_name,
    password=password,
)

user = models.User(
    person=person,
    is_staff=True,
    is_admin=True,
)
