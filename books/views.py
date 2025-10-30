from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    avg_rating = books.aggregate(Avg("rating"))
    return render(request, "books/index.html", {
        "books": books,
        "num_books": books.count(),
        "avg_rating": avg_rating

    })

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "books/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestseller
        })
