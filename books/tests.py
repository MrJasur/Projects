from django.urls import reverse
from django.test import TestCase
from .models import  Book

# Create your tests here.
class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response, 'No books found.')

    def test_book_list(self):
        Book.objects.create(title='Book1', description="Descrition1", isbn='1234561')
        Book.objects.create(title='Book2', description="Descrition2", isbn='1234562')
        Book.objects.create(title='Book3', description="Descrition3", isbn='1234563')

        response = self.client.get(reverse("books:list"))
        print(response)
        books = Book.objects.all()
        for x in books:
            self.assertContains(response, x.title)

    def test_detail_page(self):
        book = Book.objects.create(title='Book1', description="Descrition1", isbn='1234561')
        response = self.client.get(reverse('books:detail', kwargs={'id':book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)
