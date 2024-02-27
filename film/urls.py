from django.urls import path, include
from film.views import FilmListView, FilmCreateView, FilmEditView, film_delete

app_name = 'film'

urlpatterns = [
    path('', FilmListView.as_view(), name='list_view'),
    path('create-film/', FilmCreateView.as_view(), name='create_view'),
    path('edit-film/<int:pk>/', FilmEditView.as_view(), name='edit_view'),
    path('delete-film/<int:pk>/', film_delete, name='delete_view'),

    path('', include('film.modules.actors.urls')),
    path('', include('film.modules.director.urls')),

]