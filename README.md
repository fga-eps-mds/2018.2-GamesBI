# Games BI

[![Build Status](https://travis-ci.org/fga-eps-mds/2018.2-GamesBI.svg?branch=master)](https://travis-ci.org/fga-eps-mds/2018.2-GamesBI)
[![Maintainability Status](https://api.codeclimate.com/v1/badges/8c2acf5fb7871faf9e0f/maintainability)](https://codeclimate.com/github/fga-eps-mds/2018.2-GamesBI/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/fga-eps-mds/2018.2-GamesBI/badge.svg?branch=HEAD)](https://coveralls.io/github/fga-eps-mds/2018.2-GamesBI?branch=HEAD)


# Getting started

Before anything, you need to install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/). After installing those, you'll be able to start contributing to this project.

# Starting the application

It's as easy as:

Running migrations
```bash
$ make migrations
$ make migrate
```
And then

```bash
$ make up
```

And after you download all the necessary dependencies the application will be running locally.

You can also build your docker container without executing it with:

```bash
$ make build
```

And you can execute without showing any logs with:
```bash
$ (sudo) docker-compose up -d
```

# Other commands

If you want to execute some django commands inside your docker container, use:
```bash
$ (sudo) docker-compose exec web [command]
```

These commands can be:
```bash
python manage.py test
python manage.py createapp your-app
```
or any other supported by Django.

# More about the project
This project aims to offer a competitive BI for games. This includes, game development, content creation for youtube and twitch and whether you should invest in a game if you're a publisher.

A lot of its design ideas came from other sites, for example, [steamspy](steamspy.com). Although we're not only using information from Steam, but also from Youtube, Twitch and IGDB, which is another API for game data.

Our belief is that there isn't a cross-platform and helpfull BI tool for games out there. Which is why our main goal is to deliver this very such thing, and also make it acessible for everyone willing to use it.
