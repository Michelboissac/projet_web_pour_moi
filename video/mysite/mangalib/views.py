from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse        #permet d'afficher du html
from django.template import loader          #charge fichiers html
from .models import Book                    #import book de models base de donnée
# Create your views here.


def index(request):
    context = {"books": Book.objects.all()} #{"message": "hello"}                             #on pourra utiliser la variable message pour afficher hello ds le html
    #template = loader.get_template("mangalib/index.html")       #trouve le html
    return render(request, "mangalib/index.html", context) #HttpResponse(template.render(context,request))



def show(request, book_id):
    context = {"book" : get_object_or_404(Book, pk = book_id)}
    return render(request,"mangalib/show.html",context)
