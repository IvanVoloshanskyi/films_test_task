from django.urls import path
from film.modules.actors.views import ActorCreateView, actor_delete, ActorListView, ActorUpdateView

app_name = 'actors'

urlpatterns = [
    path('actors/', ActorListView.as_view(), name='actors-list'),
    path('add-actor/', ActorCreateView.as_view(), name='add-actor'),
    path('delete-actor/<int:pk>', actor_delete, name='delete-actor'),
    path('update-actor/<int:pk>', ActorUpdateView.as_view(), name='update-actor')
]
