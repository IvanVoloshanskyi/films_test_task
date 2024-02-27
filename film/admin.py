from django.contrib import admin
from film.models import Movie, Director, Actor

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
