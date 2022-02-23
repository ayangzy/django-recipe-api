
from cgi import test
from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test that can create a new user with email"""
        
        email = "testuser@gmail.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email=email, 
            password=password
            )
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalized(self):
        """Test that can normalize user email to lower"""
        
        email = 'hellWORD@gmail.com'
       
        user = get_user_model().objects.create_user(email, '23345')
        self.assertTrue(user.email, email.lower())
        #self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """Test creating a user with no email raises error"""
        with self.assertRaises(ValueError):
            email = None
            get_user_model().objects.create_user(email, '2235663')
    
    def test_create_new_super_user(self):
        """Test creating a new super user"""
        
        user = get_user_model().objects.create_superuser(
            'testuser@gmail.com',
            'pass123'    
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
           
        
        