from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from CrossData.API.models import *

class EndpointPOSTTestCase(APITestCase):

    def setUp(self):

        self.url = reverse("games_view")

        self.data = [
            {
                "id_steam": 123,
                "name": "Test 1",
                "positive_reviews_steam": 1923123,
                "negative_reviews_steam": 12121,
                "owners": 130000,
                "average_forever": 2127,
                "average_2weeks": 132,
                "price": "0",
                "languages": [
                    "mandarim", "espanhol"
                ],
                "genres": [
                    "tiro", "porrada"
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

        self.data_2 = [
            {
                "id_steam": 123,
                "name": "Test 2",
                "positive_reviews_steam": 1923123,
                "negative_reviews_steam": 12121,
                "owners": 130000,
                "average_forever": 2127,
                "average_2weeks": 132,
                "price": "0",
                "languages": [
                    "mandarim", "espanhol"
                ],
                "genres": [
                    "tiro", "porrada"
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

        self.data_ok_2 = [
            {
                "id_steam": 94123,
                "name": "Test 2",
                "positive_reviews_steam": 1923123,
                "negative_reviews_steam": 12121,
                "owners": 130000,
                "average_forever": 2127,
                "average_2weeks": 132,
                "price": "0",
                "languages": [
                    "mandarim", "espanhol"
                ],
                "genres": [
                    "tiro", "porrada"
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

    def tearDown(self):

        Game.objects.all().delete()

    def test_status_code(self):

        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_status_code_not_created(self):

        response = self.client.post(self.url, self.data_2, format='json')
        self.assertNotEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_game_data_persistence(self):

        self.client.post(self.url, self.data, format='json')
        self.assertEqual(Game.objects.all().count(), 1)

    def test_game_data_not_persistence(self):

        self.client.post(self.url, self.data_2, format='json')
        self.assertNotEqual(Game.objects.all().count(), 0)

    def test_steam_data_persistence(self):

        self.client.post(self.url, self.data, format='json')
        self.assertEqual(InfoSteam.objects.all().count(), 1)
        for info in InfoSteam.objects.all():
            self.assertEqual(info.game.name, self.data[0]['name'])

    def test_steam_data_not_persistence(self):

        self.client.post(self.url, self.data_2, format='json')
        self.assertNotEqual(InfoSteam.objects.all().count(), 0)

    def test_youtube_data_persistence(self):

        self.client.post(self.url, self.data, format='json')
        self.assertEqual(InfoYoutube.objects.all().count(), 1)
        for info in InfoYoutube.objects.all():
            self.assertEqual(info.game.name, self.data[0]['name'])

    def test_youtube_data_not_persistence(self):

        self.client.post(self.url, self.data_2, format='json')
        self.assertNotEqual(InfoYoutube.objects.all().count(), 0)

    def test_twitch_data_persistence(self):

        self.client.post(self.url, self.data, format='json')
        self.assertEqual(InfoTwitch.objects.all().count(), 1)
        for info in InfoTwitch.objects.all():
            self.assertEqual(info.game.name, self.data[0]['name'])

    def test_twitch_data_not_persistence(self):

        self.client.post(self.url, self.data_2, format='json')
        self.assertNotEqual(InfoTwitch.objects.all().count(), 0)

    def test_stream_data_persistence(self):

        self.client.post(self.url, self.data, format='json')
        self.assertEqual(TwitchStream.objects.all().count(), 1)
        for info in TwitchStream.objects.all():
            self.assertEqual(info.game.name, self.data[0]['name'])

    def test_stream_data_not_persistence(self):

        self.client.post(self.url, self.data_2, format='json')
        self.assertNotEqual(TwitchStream.objects.all().count(), 0)

    def test_data_duplication(self):
        self.client.post(self.url, self.data_2, format='json')
        self.client.post(self.url, self.data_ok_2, format='json')
        self.assertEqual(Game.objects.all().count(), 1)

    def test_data_not_duplication(self):
        self.client.post(self.url, self.data_2, format='json')
        self.client.post(self.url, self.data_ok_2, format='json')
        self.assertNotEqual(Game.objects.all().count(), 2)
