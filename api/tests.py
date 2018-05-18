
# /api/tests.py

from django.test import TestCase
from .models import User, Account, Donor, Blood, Request, Notification


class RgistrationTestCase (TestCase):
    def setUp(self):
        User.objects.create(email="a.hadi@se15.qmul.co.uk", first_name ='Abdul', last_name ='Hadi', password ='123456aa', is_donor='True')
        User.objects.create(email="mile_end @yahoo.com", first_name ='Mile End', last_name ='Hospital', password ='123456aa', is_donor ='False')

    #Test created user
    def test_user_registration(self):
        user1 = User.objects.get(email="a.hadi@se15.qmul.co.uk")
        user2 = User.objects.get(email="mile_end @yahoo.com")

        self.assertEqual(user1,user1) # successful test of equal user
        self.assertEqual(user1, user2) # Fail test of equal user
        self.assertNotEqual(user1, user2) # successful test of not equal user
        self.assertNotEqual(user2, user2) # Fail test of not equal user


class BloodRequestTestCase (TestCase):
    def setUp(self):
        User.objects.create(email="a.hadi@se15.qmul.co.uk", first_name='Abdul', last_name='Hadi', password='123456aa',is_donor='True')
        user1 = User.objects.get(email="a.hadi@se15.qmul.co.uk")
        Request.objects.create(user= user1, bloodGroup='O+', time='2018-06-07', bags=5)
        Request.objects.create(user= user1, bloodGroup='A+', time='2018-06-07', bags=5)

    def test_blood_request(self):
        user1 = Request.objects.get(bloodGroup ='O+')
        user2 = Request.objects.get(bloodGroup ='A+')
        self.assertEqual(user1, user2) # Test Failed
        self.assertEqual(user1, user1) # Test passed
        self.assertNotEqual(user1, user2) # Test passed
        self.assertNotEqual(user1, user1) # Test failed
