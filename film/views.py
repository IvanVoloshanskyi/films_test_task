from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from film.filters import FilmFilter
from film.models import Movie


class FilmListView(FilterView):
    model = Movie
    template_name = 'film/films.html'
    paginate_by = 25
    filterset_class = FilmFilter
    context_object_name = 'films'

    def get_queryset(self):
        queryset = super().get_queryset().select_related('director').prefetch_related('actors')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        paginator._count = len(self.filterset.qs)
        page = self.request.GET.get('page')

        try:
            films = paginator.page(page)
        except PageNotAnInteger:
            films = paginator.page(1)
        except EmptyPage:
            films = paginator.page(paginator.num_pages)

        context['films'] = films
        return context


class FilmCreateView(CreateView):
    template_name = 'film/create_film.html'
    model = Movie
    fields = ['title', 'year', 'actors', 'director']

    def get_success_url(self):
        return reverse('film:list_view')


class FilmEditView(UpdateView):
    pk_url_kwarg = 'pk'
    template_name = 'film/edit_film.html'
    model = Movie
    fields = ['title', 'year', 'actors', 'director']

    def get_success_url(self):
        return reverse('film:list_view')


def film_delete(request, pk):
    try:
        film = get_object_or_404(Movie, pk=pk)
        film.delete()
        messages.success(request, f"{film.title} deleted successfully")
        return redirect('film:list_view')
    except Exception as e:
        messages.error(request, f'Error deleting film: {e}')
        return redirect('film:list_view')
