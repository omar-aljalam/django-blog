from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) # {'rating__avg': 3.5}, since we can have multiple fields to aggregate
    return render(request, "books/index.html", {
        "books": books,
        "num_books": num_books,
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
