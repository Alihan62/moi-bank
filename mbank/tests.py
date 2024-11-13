from django.test import TestCase

# Create your tests here.
class ProfileTestCase(TestCase):
    def test_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

class TransactionTestCase(TestCase):
    def test_profile(self):
        response = self.client.get('/transaction/')
        self.assertEqual(response.status_code, 200)
class AddMoneyTestCase(TestCase):
    def test_profile(self):
        response = self.client.get('/add-money/')
        self.assertEqual(response.status_code, 200)

class RegistrationTestCase(TestCase):
    def test_profile(self):
        response = self.client.get('/registration/')
        self.assertEqual(response.status_code, 200)
class LoginTestCase(TestCase):
    def test_profile(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
