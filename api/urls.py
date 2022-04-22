from django.urls import path
from .views import BookReviewDetailAPIView, BookListAPIView

app_name = 'api'
urlpatterns = [
    path('reviews/', BookListAPIView.as_view(), name='review_list'),
    path('reviews/<int:id>/', BookReviewDetailAPIView.as_view(), name='review_detail'),
]