from django.core.management.base import BaseCommand, CommandError
from users.models import  Person, User
from getpass import getpass


class Command(BaseCommand):
    help = "Makes a new superuser (custom)"

    def handle(self, *args, **options):
        self.stdout.write("Initializing database superuser...")
        first_name = raw_input('First name: ')
        last_name = raw_input('Last name: ')
        person = Person(
            first_name=first_name,
            last_name=last_name,
        )
        person.save()
        person.refresh_from_db()
        self.stdout.write("Generated username: %s" % person.username)
        password = getpass('Enter password: ')
        password_copy = getpass('Enter password (repeat): ')

        while password != password_copy:
            password = getpass('Enter password: ')
            password_copy = getpass('Enter password (repeat): ')

        user = User(
            person=person,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()
        self.stdout.write("Successfully created new superuser %s" % person.username)
