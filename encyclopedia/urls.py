from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/new", views.new_wiki, name="new_wiki"),
    path("wiki/random", views.random_wiki, name="random_wiki"),
    path("wiki/<str:title>/edit", views.edit_wiki, name="edit_wiki"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    # path("wiki/search/", views.search_wiki, name="search_wiki")
]
