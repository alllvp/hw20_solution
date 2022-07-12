from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO
from setup_db import db


# GenreDAO
@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(db.session)

    test_gen1 = Genre(id=1, name='Жанр 1')
    test_gen2 = Genre(id=2, name='Жанр 2')
    test_gen3 = Genre(id=3, name='Жанр 3')

    genre_dao.get_one = MagicMock(return_value=test_gen1)
    genre_dao.get_all = MagicMock(return_value=[test_gen1, test_gen2, test_gen3])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao


# DirectorDAO
@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(db.session)

    test_dir1 = Director(id=1, name='Дир 1')
    test_dir2 = Director(id=2, name='Дир 2')
    test_dir3 = Director(id=3, name='Дир 3')

    director_dao.get_one = MagicMock(return_value=test_dir1)
    director_dao.get_all = MagicMock(return_value=[test_dir1, test_dir2, test_dir3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()

    return director_dao


# MovieDAO
@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(db.session)

    test_mov1 = Movie(id=1, title='Кино 1', description='Описание кино1', trailer='youtube1', year=2001, rating=0.1, genre_id=1, director_id=1)
    test_mov2 = Movie(id=2, title='Кино 2', description='Описание кино2', trailer='youtube2', year=2002, rating=0.2, genre_id=2, director_id=2)
    test_mov3 = Movie(id=3, title='Кино 3', description='Описание кино3', trailer='youtube3', year=2003, rating=0.3, genre_id=3, director_id=3)

    movie_dao.get_one = MagicMock(return_value=test_mov1)
    movie_dao.get_all = MagicMock(return_value=[test_mov1, test_mov2, test_mov3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao
