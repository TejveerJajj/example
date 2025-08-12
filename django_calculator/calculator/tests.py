from django.test import TestCase, Client
from django.urls import reverse

class CalculatorTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('calculate')

    def test_add(self):
        response = self.client.post(self.url, {'num1': 1, 'num2': 2, 'operation': 'add'})
        self.assertContains(response, '3.0')

    def test_subtract(self):
        response = self.client.post(self.url, {'num1': 2, 'num2': 1, 'operation': 'subtract'})
        self.assertContains(response, '1.0')

    def test_multiply(self):
        response = self.client.post(self.url, {'num1': 2, 'num2': 3, 'operation': 'multiply'})
        self.assertContains(response, '6.0')

    def test_divide(self):
        response = self.client.post(self.url, {'num1': 6, 'num2': 3, 'operation': 'divide'})
        self.assertContains(response, '2.0')

    def test_divide_by_zero(self):
        response = self.client.post(self.url, {'num1': 1, 'num2': 0, 'operation': 'divide'})
        self.assertContains(response, 'Error! Division by zero.')

    def test_exponent(self):
        response = self.client.post(self.url, {'num1': 2, 'operation': 'exponent'})
        self.assertContains(response, '4.0')

    def test_invalid_input(self):
        response = self.client.post(self.url, {'num1': 'a', 'num2': 'b', 'operation': 'add'})
        self.assertContains(response, 'Error! Invalid input.')

    def test_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
