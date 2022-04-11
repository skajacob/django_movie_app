"""Review views"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from movies.models import Movie
from .models import Review


@login_required
def list_reviews(request):
    reviews = Review.objects.filter(user=request.user)
    return render(request, "reviews/list.html", {"reviews": reviews})


@login_required
def review_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        stars = request.POST.get('stars')
        comments = request.POST.get('comments')
        review = Review(
            movie=movie,
            user=request.user,
            stars=stars,
            comments=comments
        )
        review.save()
        return redirect("movies:list")

    return render(request, "reviews/review_movie.html", {"movie": movie})
