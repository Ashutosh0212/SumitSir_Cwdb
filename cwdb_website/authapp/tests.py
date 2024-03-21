from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import CustomUser

class SignUpViewTest(TestCase):
    def setUp(self):
        self.signup_url = reverse('authapp:register')

    def test_signup_view_get(self):
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_view_post_valid_form(self):
        data = {
            'email': 'test@example.com',
            'agency_name': 'Test Agency',
            'agency_nature': 'Test Nature',
            'registration_number': '12345',
            'address': 'Test Address',
            'pincode': '123456',
            'contact_person_name': 'Test Person',
            'contact_person_designation': 'Test Designation',
            'contact_person_mobile': '1234567890',
            'password':'1234'
        }
        
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

        # Check if the user is created but not activated
        self.assertFalse(CustomUser.objects.get(email='test@example.com').is_active)


    def test_signup_view_post_invalid_form(self):
        # Posting empty data to the form should return to the signup page with errors
        response = self.client.post(self.signup_url, {})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
        self.assertFormError(response, 'form', 'email', 'This field is required.')
        # Other form field validations can be added similarly
