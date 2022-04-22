from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from books.models import BookReview
from .serializers import BookReviewSerializer
# Create your views here.

# bir dona kitobni API ni olish
class BookReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)

        serializer = BookReviewSerializer(book_review)
        
        return Response(data=serializer.data)

# Barcha kioblarni API ni olish
class BookReviewsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        book_reviews = BookReview.objects.all().order_by('-created_at')

        # paginator in APIView
        paginator = PageNumberPagination()
        page_obj = paginator.paginate_queryset(book_reviews, request)
        serializer = BookReviewSerializer(page_obj, many=True)

        # return Response(data = serializer.data)
        return paginator.get_paginated_response(serializer.data)

