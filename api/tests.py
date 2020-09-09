from django.test import TestCase

# Create your tests here.


from auths.models import User, Profile


class AuthTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            email="hjordan@gmail.com", password="abc")
        testuser1.save()

        test_profile = Profile.objects.create(
            user=testuser1, first_name="Hal", middle_name="Jack", last_name="Jordan")
        test_profile.save()

    def test_auth(self):
        profile = Profile.objects.get(id=1)
        user = f'{profile.user}'
        first_name = f'{profile.first_name}'
        last_name = f'{profile.last_name}'
        self.assertEqual(user, 'hjordan@gmail.com')
        self.assertEqual(first_name, 'Hal')
        self.assertEqual(last_name, "Jordan")


# Test ran in 0.216s => outcome: OK
