"""URL config for reviews"""

from django.urls import path

from . import views

app_name = "reviews"
urlpatterns = [
    path("check/", views.list_reviews, name="list"),
    path("new-review/<int:pk>", views.review_movie, name="create"),
]