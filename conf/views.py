from django.shortcuts import render
from books.models import Book, BookReview

def landing_page(request):
    return render(request, 'landing.html')

def home_page(request):
    book_review = BookReview.objects.all().order_by('created_at')
    context = {
        'book_review':book_review
    }
    return render(request, 'home.html', context)