CREATE DATABASE gamesbi;
CREATE USER gamesbi WITH PASSWORD 'gamesbi123';
ALTER ROLE gamesbi SET client_encoding TO 'utf8';
ALTER ROLE gamesbi SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE gamesbi TO gamesbi;