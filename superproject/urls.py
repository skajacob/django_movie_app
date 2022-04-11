"""superproject URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from movies import views

app_name = "movies"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("reviews/", include("reviews.urls")),
    path("movies/", include("movies.urls")),
    path("auth/", include("users.urls")),
]
