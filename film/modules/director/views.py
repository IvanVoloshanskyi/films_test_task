from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import UpdateView, CreateView
from django_filters.views import FilterView
from film.filters import DirectorFilter
from film.models import Director


class DirectorListView(FilterView):
    model = Director
    template_name = 'director/director_list.html'
    filterset_class = DirectorFilter
    queryset = Director.objects.all()
    context_object_name = 'directors'
    paginate_by = 25


class DirectorUpdateView(UpdateView):
    model = Director
    template_name = 'director/update_director.html'
    pk_url_kwarg = 'pk'
    fields = '__all__'

    def get_success_url(self):
        return reverse('film:director:director-list')


class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    template_name = 'director/create_director.html'

    def get_success_url(self):
        return reverse('film:director:director-list')


def director_delete(request, pk):
    try:
        director = get_object_or_404(Director, pk=pk)
        director.delete()
        messages.success(request, f'Successfully deleted director {director}')
        return redirect('film:director:director-list')
    except Exception as e:
        messages.error(request, f'Error to delete director {e}')
        return redirect('film:director:director-list')
