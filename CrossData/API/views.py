import requests

from rest_framework.response import Response
from rest_framework.views import APIView
from CrossData.importdata.models import *
from CrossData.importdata.serializers import *
# from .serializers import GameSerializer


class GamesView(APIView):

	'''
	Endpoint for receiving
	data and persisting it on database
	'''

	def post(self, request, format=None):

		game_list = request.data
		mensagem = {"mensagem":"jogos salvos com sucesso"}

		for game_data in game_list:

			new_game = self.save_game(game_data)

			info_youtube = self.save_info_youtube(game_data, new_game)
			info_steam = self.save_info_steam(game_data, new_game)
			info_twitch = self.save_info_twitch(game_data, new_game)
			streams = self.save_streams(game_data, new_game)

		return Response(data=mensagem)

	def save_game(self, game_data):

		if Game.objects.get(name=game_data['name']):
			print("jogo já cadastrado")
			return Game.objects.get(name=game_data['name'])

		new_game = Game(
			name=game_data['name'],
			languages_game=game_data['languages'],
			genres=game_data['genre'],
		)

		new_game.save()

		return new_game

	def save_info_youtube(self, game_data, game):

		new_info_youtube = InfoYoutube(
			game=game,
			count_videos=game_data['count_videos'],
			count_views=game_data['count_views'],
			count_likes=game_data['count_likes'],
			count_dislikes=game_data['count_dislikes'],
			count_comments=game_data['count_comments'],

		)

		new_info_youtube.save()

		return new_info_youtube

	def save_info_steam(self, game_data, game):

		new_info_steam = InfoSteam(
			game=game,
			positive_reviews_steam=game_data['positive_reviews_steam'],
			negative_reviews_steam=game_data['negative_reviews_steam'],
			owners=game_data['owners'],
			average_forever=game_data['average_forever'],
			average_2weeks=game_data['average_2weeks'],
			price=game_data['price'],
		)

		new_info_steam.save()

		return new_info_steam

	def save_info_twitch(self, game_data, game):

		new_info_twitch = InfoTwitch(
			game=game,
			viewer_count=game_data['total_views'],
		)

		new_info_twitch.save()

		return new_info_twitch

	def save_streams(self, game_data, game):

		saved_streams = []

		for stream_data in game_data['streams']:

			new_twitch_stream = TwitchStream(
				game=game,
				language_stream=stream_data['language'],
				started_at=stream_data['started_at'],
				type=stream_data['type'],
				stream_view_count=stream_data['viewer_count']
			)

			new_twitch_stream.save()

			saved_streams.append(new_twitch_stream)

		return saved_streams
