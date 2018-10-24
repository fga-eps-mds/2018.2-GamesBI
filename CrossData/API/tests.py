from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from CrossData.importdata.models import *

class EndpointPOSTTestCase(APITestCase):

	def setUp(self):

		self.url = reverse("games_view")
		
		self.data = [
			{
				"name": "Jogo Teste",
				"languages": "Ingles",
				"genre": "Ação",
				"count_videos": 10,
				"count_views": 11,
				"count_likes": 20,
				"count_dislikes": 110,
				"count_comments": 10,
				"positive_reviews_steam": 10,
				"negative_reviews_steam": 11,
				"owners": 10,
				"average_forever": 20,
				"average_2weeks": 40,
				"price": 50,
				"total_views": 70,
				"streams":[ 
					{
						"language": "Portugues",
						"started_at": "2018-09-30",
						"type": "Live",
						"viewer_count": 10
						
					} 
				]
				
			}
		]

	def tearDown(self):
		
		Game.objects.all().delete()

	def test_status_code(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_game_data_persistence(self):
		
		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(Game.objects.all().count(), 1)

	def test_steam_data_persistence(self):
		
		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(InfoSteam.objects.all().count(), 1)
		for info in InfoSteam.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_youtube_data_persistence(self):
		
		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(InfoYoutube.objects.all().count(), 1)
		for info in InfoYoutube.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_twitch_data_persistence(self):
		
		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(InfoTwitch.objects.all().count(), 1)
		for info in InfoTwitch.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_stream_data_persistence(self):
		
		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(TwitchStream.objects.all().count(), 1)
		for info in TwitchStream.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])
		
