import sqlite3
import datetime

connex = sqlite3.connect("data.db")

CREATE_MOVIES_TABLE = '''CREATE TABLE IF NOT EXISTS movies (id INTEGER, title TEXT, release_date TIMESTAMP, PRIMARY KEY(id));'''
CREATE_WATCHED_TABLE = '''CREATE TABLE IF NOT EXISTS watched (watcher_name TEXT, movie_id INTEGER, PRIMARY KEY(watcher_name));'''
CREATE_USERS_TABLE = '''CREATE TABLE IF NOT EXISTS users (username TEXT, movie_id INTEGER, FOREIGN KEY(username) REFERENCES watched(watcher_name), FOREIGN KEY(movie_id) REFERENCES movies(id)'''
INSERT_MOVIE = '''INSERT INTO movies (title, release_date) VALUES (?, ?);'''
INSERT_WATCHED_MOVIE = '''INSERT into watched (watcher_name, movie_id) values (?, ?);'''
SELECT_ALL_MOVIES = '''SELECT * FROM movies;'''
SELECT_UPCOMING_MOVIES = '''SELECT * FROM movies WHERE release_date > ?;'''
SELECT_WATCHED_MOVIES = '''
SELECT movies.*,
FROM movies 
JOIN watched
ON movies.id = watched.movie_id
JOIN users
ON watched.watcher_name = users.username
WHERE users.username = ?;'''
SET_WATCHED = '''UPDATE movies SET watched = 1 WHERE title = ?;'''
DELETE_MOVIE = '''DELETE FROM movies WHERE title = ?;'''
INSERT_USER = '''INSERT INTO users (username) values (?);'''

def create_tables():
    with connex:
        connex.execute(CREATE_MOVIES_TABLE)
        connex.execute(CREATE_WATCHED_TABLE)
        connex.execute(CREATE_USERS_TABLE)

def add_movie(title, release_date):
    with connex:
        connex.execute(INSERT_MOVIE,(title, release_date))

def get_movies(upcoming=False):
    with connex:
        cursor = connex.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
            return cursor.fetchall()
        else:
            cursor.execute(SELECT_ALL_MOVIES)
            return cursor.fetchall()


def watch_movie(user, movie_id):
    with connex:
        connex.execute(INSERT_WATCHED_MOVIE, (user, movie_id))

def get_watched_movie(username):
    with connex:
        cursor = connex.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()

def add_user(username):
    with connex:
        connex.execute(INSERT_USER,(username,))