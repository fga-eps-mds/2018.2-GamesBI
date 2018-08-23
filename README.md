# Games BI

[![Build Status](https://travis-ci.org/fga-eps-mds/2018.2-GamesBI.svg?branch=master)](https://travis-ci.org/fga-eps-mds/2018.2-GamesBI)
[![Maintainability Status](https://api.codeclimate.com/v1/badges/8c2acf5fb7871faf9e0f/maintainability)](https://codeclimate.com/github/fga-eps-mds/2018.2-GamesBI/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/fga-eps-mds/2018.2-GamesBI/badge.svg?branch=master)](https://coveralls.io/github/fga-eps-mds/2018.2-GamesBI?branch=master)


# Getting started

Before anything, you need to install [docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/). After installing those, you'll be able to start contributing to this project.

# Starting the application

It's as easy as:
```bash
$ (sudo) docker-compose up
```

And after you download all the necessary dependencies the application will be running locally.

You can also build your docker container without executing it with:

```bash
$ (sudo) docker-compose build
```

And you can execute without showing any logs with:
```bash
$ (sudo) docker-compose up -d
```

# Other commands

If you want to execute some django commands inside your docker container, use:
```bash
$ (sudo) docker-compose run web [command]
```

These commands can be:
```bash
python manage.py test
python manage.py createapp your-app
```
or any other supported by Django.
