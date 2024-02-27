from django.urls import path
from .views import DirectorListCreateView, DirectorRetrieveUpdateDestroyView, api_overview
from .views import ActorListCreateView, ActorRetrieveUpdateDestroyView
from .views import FilmListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('', api_overview, name='api-overview'),

    path('directors/', DirectorListCreateView.as_view(), name='director-list-create'),
    path('directors/<int:pk>/', DirectorRetrieveUpdateDestroyView.as_view(), name='director-detail'),

    path('actors/', ActorListCreateView.as_view(), name='actor-list-create'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail'),

    path('film/', FilmListCreateView.as_view(), name='film-list-create'),
    path('film/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='film-detail'),
]
