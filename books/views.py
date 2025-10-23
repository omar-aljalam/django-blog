from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404

# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", {
        "books": books
    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "books/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestseller
        })
