from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^visited$', views.places_visited, name='places_visited'),
    url(r'^isvisited$', views.place_is_visited, name='place_is_visited'),
    url(r'^edit/(?P<pk>\d+)/$', views.place_to_edit, name='edit_detail'),
]
