from django.shortcuts import render
from django.urls import reverse_lazy 
from django.views.generic import (ListView, DetailView, CreateView, DeleteView, UpdateView,)
from .models import Book


class ListBookView(ListView):
    template_name = 'book/book_list.html'
    model=Book


class DetailBookView(DetailView):
    template_name = 'book/book_detail.html'
    model = Book
    # このモデルってmodels.py?


class CreateBookView(CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category')
    # 操作が完了した後にどこのページに飛ぶのかを決める
    success_url = reverse_lazy('list-book')


class DeleteBookView(DeleteView):
    template_name = 'book/book_confirmdelete.html'
    model = Book
    # 操作が完了した後にどこのページに飛ぶのかを決める
    success_url = reverse_lazy('list-book')
    

class UpdateBookView(UpdateView):
    model = Book
    fields = ('title', 'text', 'category')
    template_name = 'book/book_update.html'
    # 操作が完了した後にどこのページに飛ぶのかを決める
    success_url = reverse_lazy('list-book')
    

def index_view(request):
    print('index_view is called')
    return render(request, 'book/index.html',{'somedata':100})
    
