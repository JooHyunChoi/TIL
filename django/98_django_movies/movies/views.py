from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.


def index(request):
    movie = Movie.objects.all()[::-1]
    context = {'movie' : movie}
    return render(request , 'movies/index.html',context)


def new(request):
    return render(request , 'movies/new.html')

def create(request):
    title = request.POST.get('title')
    title_en = request.POST.get('title_en')
    audience = request.POST.get('audience')
    open_date = request.POST.get('open_date')
    genre = request.POST.get('genre')
    watch_grade = request.POST.get('watch_grade')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    discription = request.POST.get('discription')
    movie = Movie(title = title , title_en = title_en,audience = audience,
    open_date = open_date,genre = genre,watch_grade = watch_grade,
    score = score,poster_url = poster_url,discription = discription)
    movie.save()

    return redirect('/movies/')

def detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie
    }
    return render(request , 'movies/detail.html' , context)

def edit(request,movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    context = {
        'movie' : movie
    }
    return render(request , 'movies/edit.html' , context)
def update(request, movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    movie.title = request.POST.get('title')
    movie.title_en = request.POST.get('title_en')
    movie.audience = request.POST.get('audience')
    movie.open_date = request.POST.get('open_date')
    movie.genre = request.POST.get('genre')
    movie.watch_grade = request.POST.get('watch_grade')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.discription = request.POST.get('discription')

    movie.save()

    return redirect('/movies/')