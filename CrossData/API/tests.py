from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from CrossData.importdata.models import *

class EndpointPOSTTestCase(APITestCase):

	def setUp(self):

		self.url = reverse("games_view")
		
		self.data = [
			{
			    'id_steam': 10,
				"name": "jogo teste",
				"language": "ingles",
				"genre": "ação",
				"count_videos": 10,
				"count_views": 11,
				"count_likes": 20,
				"count_dislikes": 110,
				"count_comments": 10,
				"positive_reviews_steam": 10,
				"negative_reviews_steam": 11,
				"owners": 10,
				"main_image": 'google.com',
				"screenshots": [ 
				{
					'url': "https://steamcdn-a.akamaihd.net/steam/apps/570/ss_86d675fdc73ba10462abb8f5ece7791c5047072c.600x338.jpg?t=1536248487",
					'palette': [ 
					{
						'r': 138,
						'g': 166,
						'b': 82,
						'hex': "#8aa652"
					}],
				}],
				"release_date":  "9 jul, 2013",
                "r_average": 10,
                "g_average": 10,
                "b_average": 10,
				"average_forever": 20,
				"average_2weeks": 40,
				"price": 50,
				"total_views": 70,
				"streams":[
					{
						"language": "portugues",
						"started_at": "2018-09-30",
						"type": "live",
						"viewer_count": 10
					}
				]

			}
		]
		
		self.data_2 = [
			{
			    'id_steam': 10,
				"name": "jogo teste",
				"language": "ingles",
				"count_videos": 10,
				"count_views": 11,
				"count_likes": 20,
				"count_dislikes": 110,
				"count_comments": 10,
				"positive_reviews_steam": 10,
				"negative_reviews_steam": 11,
				"owners": 10,
				"main_image": 'google.com',
				"screenshots": [ 
				{
					'url': "https://steamcdn-a.akamaihd.net/steam/apps/570/ss_86d675fdc73ba10462abb8f5ece7791c5047072c.600x338.jpg?t=1536248487",
					'palette': [ 
					{
						'r': 138,
						'g': 166,
						'b': 82,
						'hex': "#8aa652"
					}],
				}],
				"release_date":  "9 jul, 2013",
                "r_average": 10,
                "g_average": 10,
                "b_average": 10,
				"average_forever": 20,
				"average_2weeks": 40,
				"price": 50,
				"total_views": 70,
				"streams":[
					{
						"language": "portugues",
						"started_at": "2018-09-30",
						"type": "live",
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

	def test_status_code_not_created(self):

		response = self.client.post(self.url, self.data_2, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_game_data_persistence(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(Game.objects.all().count(), 1)

	def test_game_data_not_persistence(self):

		response = self.client.post(self.url, self.data_2, format='json')
		self.assertEqual(Game.objects.all().count(), 0)

	def test_steam_data_persistence(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(InfoSteam.objects.all().count(), 1)
		for info in InfoSteam.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_steam_data_not_persistence(self):

		response = self.client.post(self.url, self.data_2, format='json')
		self.assertEqual(InfoSteam.objects.all().count(), 0)

	def test_youtube_data_persistence(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(InfoYoutube.objects.all().count(), 1)
		for info in InfoYoutube.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_youtube_data_not_persistence(self):

		response = self.client.post(self.url, self.data_2, format='json')
		self.assertEqual(InfoYoutube.objects.all().count(), 0)

	def test_twitch_data_persistence(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(InfoTwitch.objects.all().count(), 1)
		for info in InfoTwitch.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_twitch_data_not_persistence(self):

		response = self.client.post(self.url, self.data_2, format='json')
		self.assertEqual(InfoTwitch.objects.all().count(), 0)

	def test_stream_data_persistence(self):

		response = self.client.post(self.url, self.data, format='json')
		self.assertEqual(TwitchStream.objects.all().count(), 1)
		for info in TwitchStream.objects.all():
			self.assertEqual(info.game.name, self.data[0]['name'])

	def test_stream_data_not_persistence(self):

		response = self.client.post(self.url, self.data_2, format='json')
		self.assertEqual(TwitchStream.objects.all().count(), 0)
