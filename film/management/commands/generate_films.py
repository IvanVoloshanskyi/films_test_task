import requests
from django.core.management.base import BaseCommand
from film.models import Director, Movie, Actor
from variables_from_env import OBDB_API_KEY
import random


class Command(BaseCommand):
    help = 'Populates the database with movies from OMDB API'

    def handle(self, *args, **kwargs):

        for movie_id in range(100):
            film_ids = random.randint(1270000, 1290000)
            url = f'http://www.omdbapi.com/?apikey={OBDB_API_KEY}&i=tt{film_ids}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                director, _ = Director.objects.get_or_create(name=data['Director'])
                movie, created = Movie.objects.get_or_create(
                    title=data['Title'],
                    year=data['Year'],
                    director=director,
                )

                actors_names = data['Actors'].split(', ')
                for actor_name in actors_names:
                    actor, _ = Actor.objects.get_or_create(name=actor_name)
                    movie.actors.add(actor)

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added movie: {movie.title}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Movie already exists: {movie.title}"))
            else:
                self.stderr.write(self.style.ERROR(f"Failed to fetch data for movie with ID: {movie_id}"))
