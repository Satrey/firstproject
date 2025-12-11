from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.base import TemplateView

from firstapp.forms import BookForm

from .models import Book

# def index(request):
#     return render(request, 'base.html')

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

def getbook(request, author):
    book = Book.objects.get(author=author)
    form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'bookform.html', context)

def addbook(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data['title']
            author = data['author']
            price = data['price']
            publisher = data['publisher']
            book = Book(title=title, author=author, price=price, publisher=publisher)
            book.save()

            return HttpResponse('<h2>Book added successfully</h2>')


        context = {'form': form}
        return render(request, 'bookform.html', context)
    

class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = {"name" : self.kwargs['name']}
        return context