from django.urls import reverse
from django.test import TestCase
from .models import  Book

# Create your tests here.
class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse('books:list'))

        self.assertContains(response, 'No books found.')

    def test_book_list(self):
        book1 = Book.objects.create(title='Book1', description="Descrition1", isbn='1234561')
        book2 = Book.objects.create(title='Book2', description="Descrition2", isbn='1234562')
        book3 = Book.objects.create(title='Book3', description="Descrition3", isbn='1234563')

        response = self.client.get(reverse("books:list") + "?page_size=2")

        books = [book1, book2]
        for x in books:
            self.assertContains(response, x.title)

        response = self.client.get(reverse("books:list") + "?page=2&page_size=2")
        self.assertContains(response, book3.title)

    def test_detail_page(self):
        book = Book.objects.create(title='Book1', description="Descrition1", isbn='1234561')
        response = self.client.get(reverse('books:detail', kwargs={'id':book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)


    def test_search_book(self):
        book1 = Book.objects.create(title='Book1', description="Descrition1", isbn='1234561')
        book2 = Book.objects.create(title='Book2', description="Descrition2", isbn='1234562')
        book3 = Book.objects.create(title='Book3', description="Descrition3", isbn='1234563')

        response = self.client.get(reverse('books:list') + "?q=Book1")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('books:list') + '?q=Book2')
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)


        response = self.client.get(reverse('books:list') + '?q=Book3')
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book2.title)