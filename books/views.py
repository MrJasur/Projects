from django.shortcuts import render
from django.views import View
from .models import Book
from django.core.paginator import Paginator

# Create your views here.
class BooksView(View):
    def get(self, request):
        books=Book.objects.all().order_by('id')

        # Search
        search_query = request.GET.get('q', '') #oxiridagi bosh string inpute da None chiqmasligi uchun
        if search_query:
            books = books.filter(title__icontains = search_query)

        # pagination
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)
        
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            'page_obj':page_obj,
            'search_query':search_query,
        }
        return render(request, 'books/list.html', context=context)


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context={
            'book':book,
        }
        return render(request, 'books/detail.html', context)