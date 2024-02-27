from django.urls import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from film.filters import DirectorFilter, ActorFilter, FilmFilter
from film.models import Movie, Director, Actor
from .serializers import MovieSerializer, DirectorSerializer, ActorSerializer


@api_view(['GET'])
def api_overview(request):
    """
    Список доступних ендпоінтів API
    """
    api_urls = {
        'Directors List/Create': reverse('director-list-create', request=request),
        'Directors Retrieve/Update/Delete': reverse('director-detail', kwargs={'pk': 1}, request=request),
        'Actors List/Create': reverse('actor-list-create', request=request),
        'Actors Retrieve/Update/Delete': reverse('actor-detail', kwargs={'pk': 1}, request=request),
        'Films List/Create': reverse('film-list-create', request=request),
        'Films Retrieve/Update/Delete': reverse('film-detail', kwargs={'pk': 1}, request=request),
    }
    return Response(api_urls)


class FilmListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FilmFilter
    pagination_class = PageNumberPagination
    pagination_class.page_size = 25


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class DirectorListCreateView(FilmListCreateView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filterset_class = DirectorFilter


class DirectorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorListCreateView(FilmListCreateView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filterset_class = ActorFilter


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
