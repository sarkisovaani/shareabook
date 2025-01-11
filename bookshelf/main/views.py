from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Books
from .forms import BooksForm

from django.conf import settings
import os

def serve_favicon(request):
    file_path = os.path.join(settings.BASE_DIR, 'static/img/favicon.ico')
    with open(file_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/x-icon")

def index(request):
    books = Books.objects.order_by('-id')
    for i in range(len(books)):
        books[i].x = (i % 4)*480
        books[i].y = 542 + (i // 4)*314
    return render(request, "main/index.html", {'books': books})

def add(request):
    error = ''
    if request.method == 'POST':
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'

    form = BooksForm()
    data = {
        'form' : form,
        'error': error
    }
    return render(request, "main/add.html", data)

def search(request):
    books = Books.objects.order_by('writer')
    for i in range(len(books)):
        books[i].x = (i % 4)*480
        books[i].y = 497 + (i // 4)*314
    return render(request, "main/search.html", {'books': books})

def exchange(request):
    id = request.GET.get('book', 'default')
    books = Books.objects.get(pk=id)
#    desc = books.description[0:450] + "..."
#    books.description = desc
    return render(request, "main/exchange.html", {'books': books})
