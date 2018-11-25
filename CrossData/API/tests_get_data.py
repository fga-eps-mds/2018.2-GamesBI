from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from CrossData.API.models import *

class EndpointGETTestCase(APITestCase):

	def setUp(self):

		self.data = [
	{
		"id_steam": 123,
		"name": "Test 1",
		"positive_reviews_steam": 49223,
		"negative_reviews_steam": 12121,
		"owners": 130000,
		"average_forever": 2127,
		"average_2weeks": 132,
		"price": "0",
		"languages": [
			"mandarim", "espanhol"
		],
		"genres": [
			"Action"
		],
		"main_image": "google.com",
		"screenshots": [
			{
				"url": "https://steamcdn-a.akamaihd.net/steam/apps/570/ss_86d675fdc73ba10462abb8f5ece7791c5047072c.600x338.jpg?t=1536248487",
				"palette": [
					{
						"r": 8,
						"g": 16,
						"b": 2,
						"hex": "#1aa741"
					},
					{
						"r": 34,
						"g": 12,
						"b": 37,
						"hex": "#2e204d"
					},
					{
						"r": 22,
						"g": 48,
						"b": 34,
						"hex": "#484454"
					},
					{
						"r": 121,
						"g": 80,
						"b": 254,
						"hex": "#b5b49a"
					},
					{
						"r": 19,
						"g": 26,
						"b": 21,
						"hex": "#3b4233"
					}
				]
			},
		],
		"release_date": "1 Feb, 1999",
		"r_average": 83,
		"g_average": 82,
		"b_average": 74,
		"count_videos": 1,
		"count_views": 2609773,
		"count_likes": 5555,
		"count_dislikes": 1107,
		"count_comments": 4152,
		"total_views": 46939,
		"streams": [
			{
				"language": "en",
				"game_id": "29595",
				"started_at": "2018-11-03T12:00:06Z",
				"type": "live",
				"viewer_count": 23661
			},
		]
	},
]

		self.url_graphic = reverse("get_data", kwargs={'graphtype':'line', 'yaxis':'average_2weeks', 'xaxis':'games'})
		self.url_graphic_name = reverse("get_game_data", kwargs={'graphtype':'line', 'yaxis':'average_2weeks', 'xaxis':'games', 'name':'Test 1'})
		self.url_graphic_yt = reverse("get_game_data", kwargs={'graphtype':'line', 'yaxis':'count_views', 'xaxis':'games', 'name':'Test 1'})
		self.url_table_tn = reverse("get_table_data", kwargs={'table_type':'trendingnow'})
		self.url_table_mw = reverse("get_table_data", kwargs={'table_type':'mostwatched'})
		self.url_table_s = reverse("get_table_data", kwargs={'table_type':'sales'})
		self.url_table_pt = reverse("get_table_data", kwargs={'table_type':'playedtime'})
		self.url = reverse("games_view")
		self.url_genres = reverse("genres")
		self.url_colors = reverse ("genre_colors") + '?genre=Action&color=r'
		self.url_name = reverse("games_view") + '?name=Test 1'
		self.url_name_partial = reverse("games_view") + '?name=&partial'

	def tearDown(self):

		Game.objects.all().delete()


	def test_graphic_status_code(self):

		response = self.client.get(self.url_graphic)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_graphic_return_json(self):

		self.client.post(self.url, self.data, format='json')
		json_ideal_return = {'x_axis': ["Test 1"], 'y_axis': [132]}
		response = self.client.get(self.url_graphic)
		self.assertEqual(response.data, json_ideal_return)

	def test_table_status_code_200(self):

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_table_tn)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_graphic_return_not_null(self):

		json_ideal_return = {'x_axis': [], 'y_axis': []}

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_graphic)
		self.assertNotEqual(response.data, json_ideal_return)

	def test_table_return_not_null(self):

		json_not_ideal_return = {'x_axis': [], 'y_axis': []}

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_table_tn)
		self.assertNotEqual(response.data, json_not_ideal_return)

	def test_table_most_watched(self):

		json_ideal_return = [{
			"game": "Test 1",
	        "owners": 130000,
	        "price": 0,
	        "positive_reviews_steam": 49223,
	        "youtube_views": 2609773,
	        "youtube_count_likes": 5555,
	        "youtube_count_dislikes": 1107,
	        "twitch_viewer_count": 46939
		}]

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_table_mw)
		self.assertEqual(response.data, json_ideal_return)
	'''
	def test_table_sales(self):

		json_ideal_return = [{
			"game": "Test 1",
			"owners": 130000,
			"price": 0,
			"positive_reviews_steam": 49223,
			"youtube_views": 2609773,
			"youtube_count_likes": 5555,
			"youtube_count_dislikes": 1107,
			"twitch_viewer_count": 46939
		}]

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_table_s)
		self.assertEqual(response.data, json_ideal_return)
	'''
	def test_table_played_time(self):

		json_ideal_return = [{
			"game": "Test 1",
	        "owners": 130000,
	        "price": 0,
	        "positive_reviews_steam": 49223,
	        "youtube_views": 2609773,
	        "youtube_count_likes": 5555,
	        "youtube_count_dislikes": 1107,
	        "twitch_viewer_count": 46939
		}]

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_table_pt)
		self.assertEqual(response.data, json_ideal_return)

	def test_graphic_with_name(self):
		json_not_ideal_return = {'x_axis': ["2018/11/25"], 'y_axis': [132]}
		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_graphic_name)
		self.assertEqual(response.data, json_not_ideal_return)

	def test_function_with_youtube_attr(self):
		json_not_ideal_return = {'x_axis': ["2018/11/25"], 'y_axis': [2609773]}
		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_graphic_yt)
		self.assertEqual(response.data, json_not_ideal_return)

	def test_method_genre_colors(self):
		json_ideal_return = {'colors': [[83, 82, 74]]}

		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_colors)
		self.assertEqual(response.data, json_ideal_return)

	def test_method_get_partial_none(self):

		json_ideal_return = {'name': self.data[0]['name'], 'release_date': '1999-02-01'}
		self.client.post(self.url, self.data, format='json')
		response = self.client.get(self.url_name)
		print(response.data)
		json_response = {'name': response.data['name'], 'release_date': response.data['release_date'] }
		self.assertEqual(json_response, json_ideal_return)
