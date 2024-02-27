from django.urls import path
from film.modules.director.views import (DirectorListView, DirectorUpdateView, DirectorCreateView,
                                         director_delete)
app_name = 'director'

urlpatterns = [
    path('director/', DirectorListView.as_view(), name='director-list'),
    path('update-director/<int:pk>', DirectorUpdateView.as_view(), name='director-update'),
    path('create-director/', DirectorCreateView.as_view(), name='director-create'),
    path('delete-director/<int:pk>', director_delete, name='director-delete'),
]