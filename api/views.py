from rest_framework.views import APIView
from rest_framework.response import Response

from books.models import BookReview
from .serializers import BookReviewSerializer
# Create your views here.

# bir dona kitobni API ni olish
class BookReviewDetailAPIView(APIView):
    def get(self, request, id):
        book_review = BookReview.objects.get(id=id)

        serializer = BookReviewSerializer(book_review)
        
        return Response(data=serializer.data)

# Barcha kioblarni API ni olish
class BookReviewsAPIView(APIView):
    def get(self, request):
        book_reviews = BookReview.objects.all()
        serializer = BookReviewSerializer(book_reviews, many=True)
        return Response(data = serializer.data)

