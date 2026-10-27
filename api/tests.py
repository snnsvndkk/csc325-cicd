from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class IndexTests(APITestCase):
    def test_index_lists_endpoints(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("/api/hello/", response.json()["endpoints"])


class HelloTests(APITestCase):
    def test_hello_returns_200(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hello_returns_message(self):
        response = self.client.get(reverse("hello"))
        self.assertEqual(response.json()["message"], "Hello from CSC325!")


class HealthTests(APITestCase):
    def test_health_is_ok(self):
        response = self.client.get(reverse("health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["status"], "ok")
