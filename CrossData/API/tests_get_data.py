from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from CrossData.importdata.models import *

class EndpointGETTestCase(APITestCase):

	def setUp(self):

		self.url_graphic = reverse("get_data", kwargs={'graphtype':'line', 'yaxis':'average_2weeks', 'xaxis':'games'})
		self.url_table = reverse("get_table_data", kwargs={'table_type':'trendingnow'})

	def tearDown(self):

		Game.objects.all().delete()

	def test_graphic_status_code(self):

		response = self.client.get(self.url_graphic)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_graphic_return_json(self):

		json_ideal_return = {'x_axis': [], 'y_axis': []}
		response = self.client.get(self.url_graphic)
		self.assertEqual(response.data, json_ideal_return)

	def test_table_status_code(self):

		response = self.client.get(self.url_table)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
