from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Review
from .forms import ReviewForm
# Create your views here.

def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    review_form = ReviewForm()
    context = {
        'movie': movie,
        'review_form': review_form
    }
    return render(request, 'movies/detail.html', context)

def review_create(request, id):
    movie = get_object_or_404(Movie, id=id)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.movies = movie
        review.users = request.user
        review.save()
        return redirect('movies:detail', id)
    
def review_delete(request, review_id, movie_id):
    get_object_or_404(Review, id=review_id).delete()
    return redirect('movies:detail', movie_id)

def like(request, id):
    movie = get_object_or_404(Movie, id=id)
    user = request.user

    if user in movie.like_users.all():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    return redirect('movies:index')