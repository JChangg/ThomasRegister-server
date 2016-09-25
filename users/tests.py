from django.test import TestCase
import models as md


class PersonCreationTestCase(TestCase):
    
    def test_username_no_mid_generation(self):
        """ Tests username creation with no middle name"""
        person = md.Person(
            first_name='John',
            last_name='Doe',
        )
        person.save()
        person.refresh_from_db()
        self.assertEqual(person.username, 'jd_000')

    def test_username_generation(self):
        person = md.Person(
            first_name='John',
            middle_names='Lemon Melon Banana',
            last_name='Doe',
        )
        person.save()
        person.refresh_from_db()
        self.assertEqual(person.username, 'jlmbd_000')

    def test_username_no_last_generation(self):
        """ Tests username creation with no last name"""
        person = md.Person(
            first_name='John',
        )
        person.save()
        person.refresh_from_db()
        self.assertEqual(person.username, 'j_000')

    def test_username_clash_generation(self):
        for i in range(0, 100):
            person = md.Person(
                first_name='John',
                last_name='Doe',
            )
            person.save()
        l = md.Person.objects.filter(
            username__startswith='jd_').order_by('-username')[0]
        final_index = int(l.username.split('_')[1])
        self.assertEqual(99, final_index)


class PersonTestCase(TestCase):

    def setUp(self):
        self.person = md.Person(
            first_name='John',
            last_name='Doe'
        )
        self.person.save()

    def test_person_str(self):
        """ Username is expected to be printed """
        self.assertEqual(self.person.__str__(), 'jd_000')


class CardTestCase(TestCase):

    def setUp(self):
        self.person = md.Person(
            first_name="John",
            last_name="Doe",
        )
        self.person.save()
        # Assign a new card to the person
        self.card = md.Card(
            id=1234,
            person=self.person,
        )
        self.card.save()

    def test_card_str(self):
        """ Expected to be printed into the form of id: username"""
        self.assertEqual(self.card.__str__(), '1234: jd_000')


class UserTestFCase(TestCase):

    def setUp(self):
        self.person = md.Person(
            first_name="John",
            last_name="Doe",
        )
        self.person.save()
        self.person.refresh_from_db()
        self.user = md.User(
            person=self.person
        )
        self.user.save()

    def test_username_auto_assigned(self):
        self.assertEqual(self.user.username, self.person.username)

    def test_username_update_assigned(self):
        """ changing the username in person should update that of user"""
        self.person.username = "abc_123"
        self.person.save()
        self.person.refresh_from_db()
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, self.person.username)

