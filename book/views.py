from django.shortcuts import render, redirect
from django.contrib.auth import logout
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


def logout_view(request):
    logout(request)
    # return render(request, 'book/index.html')
    return redirect('index')

def index_view(request):
    print('index_view is called')
    # object_list = Book.objects.all()
    object_list = Book.objects.order_by('category')
    return render(request, 'book/index.html',{'object_list':object_list})
    
