from django.test import TestCase
import models as md


class PersonCreationTestCase(TestCase):
    
    def test_username_generation(self):
        person = md.Person(
            card_id=123456,
            first_name='Jamie', 
            last_name='Chang',
            password='Lemon'
        )
        person.save()
        self.assertEqual(person.username, 'jc_000')
        
    def test_username_clash_generation(self):
        for i in range(0, 100):
            person = md.Person(
                card_id=i,
                first_name='Jamie', 
                last_name='Chang',
                password='Lemon'
            )
            person.save()
        l = md.Person.objects.filter(
            username__startswith='jc_').order_by('-username')[0]
        final_index = int(l.username.split('_')[1])
        self.assertEqual(99, final_index)
