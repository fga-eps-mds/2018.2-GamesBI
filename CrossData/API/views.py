import requests

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from CrossData.importdata.models import *
from CrossData.importdata.serializers import *


class SearchGame(APIView):

	def get(self, request, format=None):
		game_name = request.GET.get('name')
		serializer = GameNameSerializer(Game.objects.filter(name__istartswith=game_name), many=True)
		return Response(serializer.data)


class GetTableData(APIView):

	def get(self, request, table_type, format=None):

		collected_data = {}

		if table_type == "trendingnow":

			collected_data = {
				'games':[],
				'owners':[],
				'price':[],
				'positive_reviews_steam':[],
				'youtube_views':[],
				'youtube_count_likes':[],
				'youtube_count_dislikes':[],
				'twitch_viewer_count':[]
			}

			games = Game.objects.order_by(
				'-infosteam__positive_reviews_steam',
				'-infoyoutube__count_views',
				'-infoyoutube__count_videos',
				'-infoyoutube__count_likes',
				'-infotwitch__viewer_count',
				'-infoyoutube__count_comments'
			)[:20]

			for game in games:

				collected_data['games'].append(game.name)
				collected_data['owners'].append(
					InfoSteam.objects.filter(game=game).order_by('-id')[0].owners
				)
				collected_data['price'].append(
					InfoSteam.objects.filter(game=game).order_by('-id')[0].price
				)
				collected_data['positive_reviews_steam'].append(
					InfoSteam.objects.filter(game=game).order_by('-id')[0].positive_reviews_steam
				)
				collected_data['youtube_views'].append(
					InfoYoutube.objects.filter(game=game).order_by('-id')[0].count_views
				)
				collected_data['youtube_count_likes'].append(
					InfoYoutube.objects.filter(game=game).order_by('-id')[0].count_likes
				)
				collected_data['youtube_count_dislikes'].append(
					InfoYoutube.objects.filter(game=game).order_by('-id')[0].count_dislikes
				)
				collected_data['twitch_viewer_count'].append(
					InfoTwitch.objects.filter(game=game).order_by('-id')[0].viewer_count
				)


		return Response(collected_data)


class GetGraphicData(APIView):

	def get(self, request, graphtype, yaxys, xaxys, format=None):

		graph_type = graphtype
		steam_attrs = list(vars(InfoSteam()).keys())
		youtube_attrs = list(vars(InfoYoutube()).keys())
		twitch_attrs = list(vars(InfoTwitch()).keys())
		streams_attrs = list(vars(TwitchStream()).keys())

		y_axys = yaxys
		x_axys = xaxys

		game_data={}

		if graph_type == "line":

			if x_axys == 'games' or y_axys=='games':
				game_data['x_axys'] = self.get_games()

			if y_axys in steam_attrs:
				game_data['y_axys'] = self.get_data(
					InfoSteam.objects.order_by('-owners','-positive_reviews_steam', 'average_2weeks')[:15],
					y_axys
				)
			if x_axys in steam_attrs:
				game_data['x_axys'] = self.get_data(
					InfoSteam.objects.order_by('-owners','-positive_reviews_steam', 'average_2weeks')[:15],
					x_axys
				)

			'''if y_axys in youtube_attrs:
				game_data['y_axys'] = self.get_data(
					InfoYoutube.objects.all().order_by('owners')[:10],
					y_axys
				)
			if x_axys in youtube_attrs:
				game_data['x_axys'] = self.get_data(
					InfoYoutube.objects.all().order_by('owners')[:10],
					x_axys
				)

			if y_axys in twitch_attrs:
				game_data['y_axys'] = self.get_data(
					InfoTwitch.objects.all().order_by('owners')[:10],
					y_axys
				)
			if x_axys in twitch_attrs:
				game_data['x_axys'] = self.get_data(
					InfoTwitch.objects.all().order_by('owners')[:10],
					x_axys
				)'''

		return Response(game_data)

	def get_data(self, db_data, attr):

		collected_data = []

		for data in db_data:

			try:
				new_data = getattr(data, attr)
				collected_data.append(new_data)
			except AttributeError:
				pass

		return collected_data

	def get_games(self):

		games = []
		steamdata = InfoSteam.objects.order_by('-owners','-positive_reviews_steam', 'average_2weeks')[:15]
		for steam_data in steamdata:
			games.append(steam_data.game.name)

		return games


class GamesView(APIView):

	'''
	Endpoint for receiving
	data and persisting it on database
	'''

	def get(self, request, format=None):
		serializer = GameNameSerializer(Game.objects.all(), many=True)
		return Response(serializer.data)


	def post(self, request, format=None):

		game_list = request.data

		if self.check_request_data(game_list):

			for game_data in game_list:

				new_game = self.save_game(game_data)

				info_youtube = self.save_info_youtube(game_data, new_game)
				info_steam = self.save_info_steam(game_data, new_game)
				info_twitch = self.save_info_twitch(game_data, new_game)
				streams = self.save_streams(game_data, new_game)

			return Response(
				data={"mensagem":"Dados salvos com sucesso"},
				status=status.HTTP_201_CREATED
			)

		return Response(
				data={"mensagem":"Erro ao Salvar dados. Alguns atributos podem estar faltando"},
				status=status.HTTP_400_BAD_REQUEST
			)

	def check_request_data(self, data):

		attrs_list = [
			"name", "languages", "genre",
			"count_videos", "count_views", "count_likes",
			"count_dislikes", "count_comments", "positive_reviews_steam",
			"negative_reviews_steam", "owners", "average_forever",
			"average_2weeks", "price", "total_views", "streams"
		]

		for record in data:
			print(record)
			for attr in attrs_list:
				if attr not in list(record.keys()):
					return False
		return True

	def save_game(self, game_data):

		try:
			Game.objects.get(name=game_data['name'])
			print("jogo já cadastrado")
			return Game.objects.get(name=game_data['name'])

		except Game.DoesNotExist:

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

		try:
			new_info_youtube.save()
			return new_info_youtube

		except ValueError:
			return False

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

		try:
			new_info_steam.save()
			return new_info_steam

		except ValueError:
			return False

	def save_info_twitch(self, game_data, game):

		new_info_twitch = InfoTwitch(
			game=game,
			viewer_count=game_data['total_views'],
		)

		try:
			new_info_twitch.save()
			return new_info_twitch

		except ValueError:
			return False

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

			try:
				new_twitch_stream.save()
				saved_streams.append(new_twitch_stream)

			except ValueError:
				return False

		return saved_streams
