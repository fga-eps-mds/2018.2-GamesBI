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

		self.data_2 = [
			{
				"languages": "Ingles",
				"genre": "Tiro",
				"count_videos": 14,
				"count_views": 19,
				"count_likes": 30,
				"count_dislikes": 5,
				"count_comments": 2,
				"positive_reviews_steam": 15,
				"negative_reviews_steam": 12,
				"owners": 9,
				"average_forever": 15,
				"average_2weeks": 30,
				"price": 60,
				"total_views": 80,
				"streams":[
					{
						"language": "Portugues",
						"started_at": "2018-09-30",
						"type": "Live",
						"viewer_count": 12
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
