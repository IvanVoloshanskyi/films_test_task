import django_filters

from film.models import Movie, Actor, Director


class FilmFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Назва')
    actors = django_filters.ModelChoiceFilter(queryset=Actor.objects.all(), label='Актори')

    class Meta:
        model = Movie
        fields = ['title', 'year', 'director', 'actors']


class ActorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Actor
        fields = ['name']


class DirectorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Director
        fields = ['name']
