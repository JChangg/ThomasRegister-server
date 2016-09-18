from users import models
from getpass import getpass


print "Initializing database superuser..."
first_name = raw_input('First name: ')
last_name = raw_input('Last name: ')
password = getpass('pw: ')

