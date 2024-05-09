from django.shortcuts import render, redirect
from .models import Movie, Series
# from django.template import loader
import random


def home(request):
    random_movie = Movie.objects.order_by('?')[:3]
    random_series = Series.objects.order_by('?')[:3]
    return render(request, 'home.html', {'random_movie': random_movie, 'random_series': random_series})


def gallery(request):
    all_movies = Movie.objects.all()
    all_series = Series.objects.all()
    return render(request, 'gallery.html', {'all_movies': all_movies, 'all_series': all_series})


def register(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'form-series':
            new_series = Series(
                title=request.POST['title'],
                genre=request.POST['genre'],
                year=request.POST['year'],
                seasons=request.POST['seasons'],
                actor=request.POST['actor'],
                producer=request.POST['producer'],
                rate=request.POST['rate'],
                message=request.POST['message'],
                img_url=request.POST['img_url']
            )
            new_series.save()
            return redirect('gallery')
        elif form_type == 'form-movies':
            new_movie = Movie(
                title=request.POST['title'],
                genre=request.POST['genre'],
                year=request.POST['year'],
                primary_actor=request.POST['primary_actor'],
                secondary_actor=request.POST['secondary_actor'],
                producer=request.POST['producer'],
                rate=request.POST['rate'],
                message=request.POST['message'],
                img_url=request.POST['img_url']
            )
            new_movie.save()
            return redirect('gallery')
    return render(request, 'register.html', {})


def movie_info(request, pk):
    movie = Movie.objects.get(id=pk)
    return render(request, 'movie_info.html', {'movie': movie})


def show_info(request, pk):
    show = Series.objects.get(id=pk)
    return render(request, 'show_info.html', {'show': show})


def remove_movie(request, pk):
    movie = Movie.objects.get(id=pk)
    movie.delete()
    return redirect('gallery')


def remove_show(request, pk):
    show = Series.objects.get(id=pk)
    show.delete()
    return redirect('gallery')
