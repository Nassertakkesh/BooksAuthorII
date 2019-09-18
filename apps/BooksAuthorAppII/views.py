from django.shortcuts import render, HttpResponse, redirect
from .models import *

def homepage(request):
    context = {
        "allbooks": Books.objects.all()
    }
    return render(request, "BooksAuthorAppII/books.html", context)

def addingbook(request):
    creatingbook = Books.objects.create(title = request.POST["titleName"], desc = request.POST["descriptionName"])
    print("hello")
    print(creatingbook)
    return redirect("/")
    
def books_page(request,id):
    print("hello world, this is nate for books ")
    context = {
        "allauthors": Books.objects.get(id = id).authors.all(),
        "book": Books.objects.get(id = id),
        "thebookclass" : Authors.objects.all(),
        "remainingauthors": Authors.objects.all().exclude(books__in=Books.objects.filter(id=int(id)))
    }
    return render(request, "BooksAuthorAppII/books_page.html", context)

def addingauthortobook(request):
    print("hello world, tryna add to the list of books")
    this_book_id = request.POST["hiddenValue"]
    this_author_id = request.POST["selectBook"]
    this_author = Authors.objects.get(id=this_author_id)
    this_book = Books.objects.get(id=this_book_id)
    print(this_book)
    print(this_author)
    this_book.authors.add(this_author)
    return redirect("/authors/"+this_book_id)
#**************************************************************************************************************************************************************************************

def authors(request):
    context = {
        "allauthors": Authors.objects.all()
    }
    return render(request, "BooksAuthorAppII/authors.html", context)

def addingauthor(request):
    creatingauthor = Authors.objects.create(first_name = request.POST["firstName"], last_name = request.POST["lastName"], notes = request.POST["notesName"])
    print("author creation")
    print(creatingauthor)
    return redirect("/authors")

def authors_page(request,id):
    print("hello world, this is nate ")
    context = {
        "allbooks": Authors.objects.get(id = id).books.all(),
        "author": Authors.objects.get(id = id),
        "theauthorclass" : Books.objects.all(),
        "remainingBooks": Books.objects.all().exclude(authors__in=Authors.objects.filter(id=int(id)))
    }
    return render(request, "BooksAuthorAppII/authors_page.html", context)

def addingbooktoauthor(request):
    print("hello world, tryna add to the list of books")
    this_author_id = request.POST["hiddenValue"]
    this_book_id = request.POST["selectBook"]
    this_author = Authors.objects.get(id=this_author_id)
    this_book = Books.objects.get(id=this_book_id)
    print(this_book)
    print(this_author)
    this_author.books.add(this_book)
    return redirect("/authors/"+this_author_id)






    # context = {
    #     "authors": Authors.objects.get(id = id).books.all(),
    #     "author": Authors.objects.get(id = id),
    #     "theauthorclass" : Books.objects.all()
    # }
    # return render(request, "BooksAuthorAppII/authors_page.html", context)








# def DisplayingBooks(request):
#     context = {
#         "allbooks": Books.objects.all()
#     }
#     return render(request, "BooksAuthorAppII/books.html", context)

# def DisplayingAuthors(request):
#     context = {
#         "allauthors": Authors.objects.all()
#     }
#     return render(request, "BooksAuthorAppII/authors.html", context)
