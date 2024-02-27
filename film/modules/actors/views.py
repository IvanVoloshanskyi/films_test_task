from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from film.filters import ActorFilter
from film.models import Actor


class ActorListView(FilterView):
    filterset_class = ActorFilter
    queryset = Actor.objects.all()
    template_name = 'actor/actors_list.html'
    context_object_name = 'actors'
    paginate_by = 25


class ActorCreateView(CreateView):
    model = Actor
    template_name = 'actor/create_actor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('film:actors:actors-list')


class ActorUpdateView(UpdateView):
    pk_url_kwarg = 'pk'
    model = Actor
    template_name = 'actor/update_actor.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('film:actors:actors-list')


def actor_delete(request, pk):
    try:
        actor = get_object_or_404(Actor, pk=pk)
        actor.delete()
        messages.success(request, f'Successfully deleted actor {actor}')
        return redirect('film:actors:actors-list')
    except Exception as e:
        messages.error(request, f'Error to delete actor {e}')
        return redirect('film:actors:actors-list')
