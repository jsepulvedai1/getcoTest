from django.test import TestCase, Client
from travels.models import Category, User, Travel
from django.urls import reverse
import json
from rest_framework import status
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler


class UserTest(TestCase):
    client = Client()

    def create_data(self):
        user = User.objects.create(
            first_name="testing",
            last_name="testing",
            email="Test@getco.com",
            password="testing"
        )
        user.save()
        self.user = user

        category = Category.objects.create(
            name="test"
        )

        self.travel = Travel.objects.create(
            status=1,
            name="travel_test",
            user=self.user,
            category=category
        )
        payload = jwt_payload_handler(self.user)
        self.token = jwt_encode_handler(payload)

    def setUp(self):
        self.create_data()

    def test_users_travel(self):
        response = self.client.get(
            reverse(
                'getco:user_travels',
                kwargs={
                    'user_id': self.user.pk
                }
            ),
            content_type='application/json',
            HTTP_AUTHORIZATION=f'JWT {self.token}'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        json_response = json.loads(response.content)
        self.assertEqual(self.travel.name, json_response[0].get('name'))
