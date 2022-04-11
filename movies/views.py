"""Movies views"""

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import DirectorForm, DirectorModelForm
from .models import Movie


def list_movies(request):
    context = {"movies": Movie.objects.all()}
    return render(request, "movies/list.html", context)


def retrieve_movie_full(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        context = {"movie": movie}
        return render(request, "movies/retrieve.html", context)
    except Movie.DoesNotExist:
        raise Http404


def retrieve_movie_shortcut(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {"movie": movie}
    return render(request, "movies/retrieve.html", context)


def create_director_with_normal_form(request):
    form = DirectorForm()
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    return render(request, "movies/create_director.html", {"form": form})


def create_director_with_model_form(request):
    form = DirectorModelForm()
    if request.method == 'POST':
        form = DirectorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    return render(request, "movies/create_director.html", {"form": form})
