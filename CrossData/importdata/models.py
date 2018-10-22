from django.db import models

class Game(models.Model):

	id = models.AutoField(
		primary_key=True
	)

	name = models.CharField(
		('Name'),
		help_text=("Game name"),
		max_length=100,
		null=True
	)

	languages_game = models.CharField(
		('Languages'),
		help_text=("Language of the game"),
		null=True,
		max_length=150
	)

	genres = models.CharField(
		('Game Genre'),
		help_text=("Name of the Game Genre"),
		max_length=50,
		null=True
	)

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

class InfoYoutube(models.Model):

	id = models.AutoField(
		primary_key=True
	)

	game = models.ForeignKey(
		Game,
		on_delete=models.CASCADE
	)

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

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return "InfoYoutube"

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Youtube Data")
	    verbose_name_plural = ("Youtube Data")


class InfoSteam(models.Model):

	id = models.AutoField(
		primary_key=True
	)

	game = models.ForeignKey(
		Game,
		on_delete=models.CASCADE
	)

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

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return "InfoSteam"

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Steam Data")
	    verbose_name_plural = ("Steam Data")


class InfoTwitch(models.Model):

	id = models.AutoField(
		primary_key=True
	)

	game = models.ForeignKey(
		Game,
		on_delete=models.CASCADE
	)
	
	viewer_count = models.IntegerField(
		('Twitch Game streams Viewer count'),
		help_text=("Number of views in stream"),
		null=True
	)

	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return "InfoTwitch"

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Twitch Data")
	    verbose_name_plural = ("Twitch Data")


class TwitchStream(models.Model):

	id = models.AutoField(
		primary_key=True
	)

	game = models.ForeignKey(
		Game,
		on_delete=models.CASCADE
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

	date = models.DateTimeField(auto_now_add=True)

	

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return "Info Stream"

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("Stream Data")
	    verbose_name_plural = ("Streams Data")
