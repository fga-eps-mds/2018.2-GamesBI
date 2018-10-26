from .models import *
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):

	class Meta:

		model = Game
		fields = ['name']


class YoutubeInfoSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = InfoYoutube
		fields = '__all__'


class SteamInfoSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = InfoSteam
		fields = '__all__'


class TwitchInfoSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = InfoTwitch
		fields = '__all__'


class TwitchStreamSerializer(serializers.ModelSerializer):

	game = GameSerializer()

	class Meta:

		model = TwitchStream
		fields = '__all__'
