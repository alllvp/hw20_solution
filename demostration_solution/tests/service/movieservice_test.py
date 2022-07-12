import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            'title': 'Кино created',
            'description': 'Описание кино created',
            'trailer': 'youtube created',
            'year': 2001,
            'rating': 0.1,
            'genre_id': 1,
            'director_id': 1
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 3,
            'title': 'Кино updated',
            'description': 'Описание кино updated',
            'trailer': 'youtube updated',
            'year': 2001,
            'rating': 0.1,
            'genre_id': 1,
            'director_id': 1
        }
        self.movie_service.update(movie_d)
