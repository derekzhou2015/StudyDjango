from django.shortcuts import render, HttpResponse, redirect
from .models import Publisher, Author, Book, AuthorDetail
from .form import PublisherAddForm, PublisherEditForm, AuthorForm, AuthorDetailForm
# Create your views here.


def index(request):
    l1 = Book.objects.all().order_by('-id')
    return render(request, 'books/index.html', {'context': l1})


def books_add(request):
    form = None
    return render(request, 'books/books_add.html', {'form': form})


def books_edit(request):
    form = None
    return render(request, 'books/books_edit.html', {'form': form})


def books_delete(request):
    id = request.GET.get('id')
    Book.objects.filter(id=id).delete()
    return redirect('./')


def authors(request):
    l1 = Author.objects.all().order_by('-id')
    return render(request, 'books/authors.html', {'context': l1})


def authors_add(request):
    form1, form2 = None, None
    if request.method == 'GET':
        form1 = AuthorForm()
        form2 = AuthorDetailForm()
    else:
        form1, form2 = AuthorForm(request.POST), AuthorDetailForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            author = Author.objects.create(**form1.cleaned_data)
            AuthorDetail.objects.create(
                author=author, **form2.cleaned_data)
            return redirect('./')
    return render(request, 'books/authors_add.html', {'form1': form1, 'form2': form2})


def authors_edit(request, id):
    author = Author.objects.get(id=id)
    detail = AuthorDetail.objects.get(author=author)
    form1, form2 = None, None
    if request.method == 'GET':
        form1 = AuthorForm({
            'name': author.name,
            'age': author.age
        })
        form2 = AuthorDetailForm({
            'gender': detail.gender,
            'tel': detail.tel,
            'address': detail.address,
            'birthday': detail.birthday
        })
    else:
        form1, form2 = AuthorForm(request.POST), AuthorDetailForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            Author.objects.filter(id=id).update(**form1.cleaned_data)
            AuthorDetail.objects.filter(
                author_id=id).update(**form2.cleaned_data)
            return redirect('../')
    return render(request, 'books/authors_add.html', {'form1': form1, 'form2': form2})


def authors_delete(request):
    id = request.GET.get('id')
    Author.objects.filter(id=id).delete()
    return redirect('./')


def publishers(request):
    l1 = Publisher.objects.all()
    return render(request, 'books/publishers.html', {'context': l1})


def publishers_add(request):
    form = None
    if request.method == 'GET':
        form = PublisherAddForm()
    else:
        form = PublisherAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop('id')
            Publisher.objects.create(**data)
            return redirect('./')
    return render(request, 'books/publishers_add.html', {'form': form})


def publishers_edit(request, id):
    obj = Publisher.objects.get(id=id)
    form = None
    if request.method == 'GET' and obj:
        form = PublisherEditForm({
            'id': obj.id,
            'name': obj.name,
            'city': obj.city,
            'email': obj.email
        })
    else:
        form = PublisherEditForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Publisher.objects.filter(id=id).update(**data)
            return redirect('../')
    return render(request, 'books/publishers_add.html', {'form': form})


def publishers_delete(request):
    id = request.GET.get('id')
    Publisher.objects.filter(id=id).delete()
    return redirect('./')
