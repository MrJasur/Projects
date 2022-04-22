from rest_framework.test import APITestCase
from rest_framework.reverse import reverse

from books.models import Book, BookReview
from users.models import CustomUserModel

# Create your tests here.
class BookViewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUserModel.objects.create(username='Coder', first_name='Jasurbek')
        self.user.set_password('abc123')
        self.user.save()


    def test_book_review_detail(self):
        book = Book.objects.create(title="Harry Potter", description='written by Joane Rowling', isbn='123456')
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="very good book")


        response = self.client.get(reverse('api:review_detail', kwargs={'id':br.id}))
        
        # review
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], br.id)
        self.assertEqual(response.data['stars_given'], 5)
        self.assertEqual(response.data['comment'], 'very good book')
        # book
        self.assertEqual(response.data['book']['id'], br.book.id)
        self.assertEqual(response.data['book']['title'], 'Harry Potter')
        self.assertEqual(response.data['book']['description'], 'written by Joane Rowling')
        self.assertEqual(response.data['book']['isbn'], '123456')
        # user
        self.assertEqual(response.data['user']['id'], self.user.id)
        self.assertEqual(response.data['user']['first_name'], 'Jasurbek')
        self.assertEqual(response.data['user']['username'], 'Coder')


    def test_book_review_list(self):
        user_two = CustomUserModel.objects.create(username='Coder2', first_name='Jasurbek')
        book = Book.objects.create(title="Harry Potter", description='written by Joane Rowling', isbn='123456')
        br = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="very good book")
        br2 = BookReview.objects.create(book=book, user=self.user, stars_given=5, comment="very good book too")

        response = self.client.get(reverse('api:review_list'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)