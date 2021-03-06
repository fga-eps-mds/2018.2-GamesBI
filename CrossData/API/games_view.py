import requests

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from CrossData.API.models import *
from CrossData.API.serializers import *
from urllib.parse import unquote
import dateutil.parser
import datetime


class GetGamesView(APIView):

    def get(self, request, format=None):
        partial = request.GET.get('partial')
        game_name = unquote(request.GET.get('name'))

        if partial is not None:
            data = GameNameSerializer(Game.objects.filter(
                name__istartswith=game_name), many=True).data
        else:
            try:
                game = Game.objects.get(name=game_name)
                data = self.all_data(game)
            except Game.DoesNotExist:
                game = None
                data = []
        return Response(data)

    '''
    Endpoint for receiving
    data and persisting it on database
    '''

    def post(self, request, format=None):
        game_list = request.data
        if self.check_request_data(game_list):
            for game_data in game_list:
                new_game = self.save_game(game_data)
                self.save_info_youtube(game_data, new_game)
                self.save_info_steam(game_data, new_game)
                self.save_info_twitch(game_data, new_game)
                self.save_streams(game_data, new_game)
            return Response(
                data={"mensagem": "Dados salvos com sucesso"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={
                    "mensagem": "Erro ao Salvar dados. Alguns atributos podem estar faltando"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def all_data(self, game):
        twitch_info = InfoTwitch.objects.filter(game=game).latest('date')
        youtube_info = InfoYoutube.objects.filter(game=game).latest('date')
        steam_info = InfoSteam.objects.filter(game=game).latest('date')
        languages = Language.objects.filter(game=game)
        genres = Genre.objects.filter(game=game)
        streams = TwitchStream.objects.filter(game=game)
        screenshots = Screenshot.objects.filter(game=game)

        lang_dict = {"languages": [x.language for x in languages]}
        genres_dict = {"genres": [x.genre for x in genres]}

        streams_array = [TwitchStreamSerializer(x).data for x in streams]
        for stream in streams_array:
            del stream['game']

        screenshots_array = [ScreenshotSerializer(x).data for x in screenshots]
        for screenshot in screenshots_array:
            palette_array = [PaletteSerializer(x).data for x in Palette.objects.filter(
                screenshot_id=screenshot['id']).defer('screenshot')]
            for palette in palette_array:
                del palette['screenshot']
            screenshot.update({'palettes': palette_array})
            del screenshot['game']

        data = {}
        data.update(GameSerializer(game).data)
        data.update(TwitchInfoSerializer(twitch_info).data)
        data.update(YoutubeInfoSerializer(youtube_info).data)
        data.update(SteamInfoSerializer(steam_info).data)
        data.update(lang_dict)
        data.update(genres_dict)
        data.update({'streams': streams_array})
        data.update({'screenshots': screenshots_array})

        if data["release_date"] is not None:
            data["release_date"] = data["release_date"].split('T')[0]

        del data["languages_game"]
        del data['game']

        return data

    def check_request_data(self, data):
        attrs_list = [
            'id_steam',
            'name',
            'positive_reviews_steam',
            'negative_reviews_steam',
            'owners',
            'average_forever',
            'average_2weeks',
            'price',
            'languages',
            'genres',
            'main_image',
            'screenshots',
            'release_date',
            'r_average',
            'g_average',
            'b_average',
            'count_videos',
            'count_views',
            'count_likes',
            'count_dislikes',
            'count_comments',
            'total_views',
            'streams'
        ]
        for record in data:
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
                r_average=game_data['r_average'],
                g_average=game_data['g_average'],
                b_average=game_data['b_average'],
                main_image=game_data['main_image'],
                release_date=self.get_release_data(game_data['release_date'])
            )
            new_game.save()
            print("Jogo salvo: {}".format(new_game.name))
            languages = self.save_languages(game_data)
            print("Salvando linguagens ...")
            for language in languages:
                print(language)
                new_game.languages_game.add(language)
            genres = self.save_genres(game_data)
            print("Salvando generos ...")
            for genre in genres:
                print(genre)
                new_game.genres.add(genre)
            self.save_screenshots(game_data, new_game)
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

    def save_languages(self, game_data):
        array_languages = []
        for language in game_data['languages']:
            try:
                Language.objects.get(language=language)
                # print("linguagem já cadastrada")
                array_languages.append(Language.objects.get(language=language))
            except Language.DoesNotExist:
                new_language = Language(
                    language=language,
                )
                new_language.save()
                array_languages.append(new_language)

        return array_languages

    def save_genres(self, game_data):
        array_genres = []
        for genre in game_data['genres']:
            try:
                Genre.objects.get(genre=genre)
                # print("Genero já cadastrado")
                array_genres.append(Genre.objects.get(genre=genre))
            except Genre.DoesNotExist:
                new_genre = Genre(
                    genre=genre,
                )
                new_genre.save()
                array_genres.append(new_genre)

        return array_genres

    def save_screenshots(self, game_data, game):
        saved_screenshots = []
        for screenshot_data in game_data['screenshots']:
            new_screenshot = Screenshot(
                game=game,
                url=screenshot_data['url'],
            )
            try:
                new_screenshot.save()
                saved_screenshots.append(new_screenshot)
                self.save_palettes(screenshot_data, new_screenshot)
            except ValueError:
                return False

        return saved_screenshots

    def save_palettes(self, screenshot_data, screenshot):
        saved_palettes = []
        for palette in screenshot_data['palette']:
            new_palette = Palette(
                screenshot=screenshot,
                r=palette['r'],
                g=palette['g'],
                b=palette['b'],
                hex=palette['hex']
            )
            try:
                new_palette.save()
                saved_palettes.append(new_palette)
            except ValueError:
                return False

        return saved_palettes

    def get_release_data(self, str_date):
        if str_date is None:
            return

        tmp_datetime = dateutil.parser.parse(str_date)

        return tmp_datetime.date()

    def convert_month_str_to_integer(self, month_str):
        if month_str in calendar.month_abbr:
            return list(calendar.month_abbr).index(month_str)
        else:
            return 1
