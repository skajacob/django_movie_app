from django.urls import path

from movies import views

app_name = "movies"

urlpatterns = [
    path("", views.list_movies, name="list"),
    path("<int:pk>", views.retrieve_movie_shortcut, name="retrieve"),
    path("director/create", views.create_director_with_model_form, name="create_director"),
]