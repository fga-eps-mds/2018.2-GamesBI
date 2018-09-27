from djongo import models

class GeneralData(models.Model):

	id = models.IntegerField(
		('ID'),
		help_text=("Id"),
		primary_key=True,
		null=False
	)

	name = models.CharField(
		('Name'),
		help_text=("Game name"),
		max_length=100,
		null=True
	)

	#IGDB
	time_to_beat = models.FloatField(
		('Time To Beat'),
		help_text=("Average time to beat the game"),
		null=True
	)

	hypes = models.IntegerField(
		('Hypes'),
		help_text=("Number of access in the game befores its release"),
		null=True
	)

	popularity = models.FloatField(
		('Popularity'),
		help_text=("Popularity of game"),
		null=True
	)

	critics_rating = models.FloatField(
		('Critics Rating'),
		help_text=("Rating based on external critic scores"),
		null=True
	)

	genres = models.CharField(
		('Game Genre'),
		help_text=("Name of the Game Genre"),
		max_length=50,
		null=True
	)

	#Steam
	positive_reviews_steam = models.IntegerField(
		('Steam Positive Reviews'),
		help_text=("Number of positive reviews at Steam"),
		null=True
	)

	negative_reviews_steam = models.IntegerField(
		('Steam Negative Reviews'),
		help_text=("Number of negative reviews at Steam"),
		null=True
	)

	owners = models.IntegerField(
		('Steam Owners'),
		help_text=("Name of the owners"),
		null=True
	)

	average_forever = models.IntegerField(
		('Average Played Time'),
		help_text=("Average forever of the game"),
		null=True
	)

	average_2weeks = models.IntegerField(
		('Average Played Time 2 weeks'),
		help_text=("Average Played Time 2 weeks of the game"),
		null=True
	)

	price = models.IntegerField(
		('Price'),
		help_text=("Price of the game"),
		null=True
	)

	languages_game = models.CharField(
		('Languages'),
		help_text=("Language of the game"),
		null=True,
		max_length=150
	)


	#YouTube
	count_videos = models.IntegerField(
		('Youtube total videos number'),
		help_text=("Number of videos found in youtube request"),
		null=True
	)

	count_views = models.IntegerField(
		('Youtube total views'),
		help_text=("Number of views summed from youtube videos"),
		null=True
	)

	count_likes = models.IntegerField(
		('Youtube total likes'),
		help_text=("Number of likes summed from youtube videos"),
		null=True
	)

	count_dislikes = models.IntegerField(
		('Youtube total dislikes'),
		help_text=("Number of dislikes summed from youtube videos"),
		null=True
	)

	count_comments = models.IntegerField(
		('Youtube total comments count'),
		help_text=("Number of comments summed from youtube videos"),
		null=True
	)

	#Twitch
	view_count = models.IntegerField(
		('Twitch users total views'),
		help_text=("Total Views couting of twitch users"),
		null=True
	)

	follows = models.IntegerField(
		('Twitch users total follows'),
		help_text=("Number of followers"),
		null=True
	)

	language_stream = models.CharField(
		('Twitch stream Language'),
		help_text=("Language of stream"),
		max_length=100,
		null=True
	)

	started_at = models.CharField(
		('Twitch stream Started date'),
		help_text=("Date when stream started"),
		max_length=100,
		null=True
	)

	type = models.CharField(
		('Twitch stream Type'),
		help_text=("Type of stream"),
		max_length=100,
		null=True
	)

	viewer_count = models.IntegerField(
		('Twitch Game streams Viewer count'),
		help_text=("Number of views in stream"),
		null=True
	)

	objects = models.DjongoManager()

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.name

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Game Data")
	    verbose_name_plural = ("Games Data")
