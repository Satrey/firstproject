from django.shortcuts import render
from django.http import HttpResponse

from .models import Book

def index(request):
    return render(request, 'base.html')

def about(request):
    return HttpResponse("<h2>Know more about FirstApp.</h2>")

def user(request, name):
    return HttpResponse(f"<h2>Hello, {name}. Welcome to thehome page of FirstApp.</h2>")

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books.html', context)

def book(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'book.html', context)

def getbook(request):
    context = {}
    return render(request, 'bookform.html', context)