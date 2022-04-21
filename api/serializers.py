from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length = 200)
    description = serializers.CharField()
    isbn = serializers.CharField(max_length = 17)

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)

class BookReviewSerializer(serializers.Serializer):
    stars_given = serializers.IntegerField(min_value=1, max_value=5)
    comment = serializers.CharField()
    book = BookSerializer()
    user = UserSerializer()