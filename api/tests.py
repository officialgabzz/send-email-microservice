from django.test import TestCase
from django.urls import resolve

# Create your tests here.
class SendMail(TestCase):
    url = resolve("api/v1/sendemail/")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

