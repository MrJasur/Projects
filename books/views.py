from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from .models import Book, BookReview
from django.core.paginator import Paginator
from .forms import BookReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BooksView(View):
    def get(self, request):
        books=Book.objects.all().order_by('id')

        # Search
        search_query = request.GET.get('q', '') #oxiridagi bosh string inpute da None chiqmasligi uchun
        if search_query:
            books = books.filter(title__icontains = search_query)

        # pagination
        page_size = request.GET.get('page_size', 2) #faqat 2 ta item chiqsin degani
        paginator = Paginator(books, page_size) #bu yerda books dan barcha booklarni olib, 1 ta pageda 2 ta kitob chiqsin degani
        page_num = request.GET.get('page', 1) #book list page ga otganda, paginator nechanchi page ni ochib berishi. Bu yerda 3
        page_obj = paginator.get_page(page_num)
        context = {
            'page_obj':page_obj,
            'search_query':search_query,
        }
        return render(request, 'books/list.html', context=context)


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm()
        context={
            'book':book,
            'review_form':review_form,
        }
        return render(request, 'books/detail.html', context)


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(data=request.POST)
        context = {
            'review_form':review_form,
        }

        if review_form.is_valid():
            BookReview.objects.create(
                book = book,
                user = request.user,
                stars_given = review_form.cleaned_data['stars_given'],
                comment = review_form.cleaned_data['comment']
            )

            return redirect(reverse('books:detail', kwargs={'id':book.id}))

        return render(request, 'books/detail.html', context)
            