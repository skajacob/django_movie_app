"""Movies app models tests"""

from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Movie, Director
from reviews.models import Review


User = get_user_model()


class TestModels(TestCase):
    @classmethod
    def setUpTestData(self):
        self.tarantino = Director.objects.create(
            first_name='Quentin',
            last_name='Tarantino',
            birthday=date(1963, 3, 27),
        )
        self.pulp_fiction = Movie.objects.create(
            name='Pulp Fiction',
            director=self.tarantino,
            release_date=date(1994, 10, 14),
        )
        self.user = User.objects.create_user(
            username="ultr4nerd",
            first_name="Mau",
            last_name="Chávez Olea",
            password="12345",
            email="mauricio@gmail.com"
        )

    def test_movie_str(self):
        self.assertEqual(str(self.pulp_fiction), 'Pulp Fiction')

    def test_movie_has_user_review(self):
        self.assertFalse(self.pulp_fiction.has_user_review(self.user))
        Review.objects.create(
            movie=self.pulp_fiction,
            user=self.user,
            stars=5,
            comments="Muy buena"
        )
        self.assertTrue(self.pulp_fiction.has_user_review(self.user))

    def test_director_full_name(self):
        self.assertEqual(self.tarantino.full_name, "Quentin Tarantino")

    def test_director_str(self):
        self.assertEqual(str(self.tarantino), "Quentin Tarantino")