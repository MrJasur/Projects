from unicodedata import name
from django.urls import path
from .views import BooksView, AddReviewView, BookDetailView

app_name='books'
urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:id>/', BookDetailView.as_view(), name='detail'),
    path('<int:id>/reviews/', AddReviewView.as_view(), name='reviews'),
]