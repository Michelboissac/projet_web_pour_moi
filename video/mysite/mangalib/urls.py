from django.urls import path     # import path
from . import views              # import le fichier view de ce repertoire avce les fcts

app_name = "mangalib"

urlpatterns = [
    path('',views.index,name='index'),  #manga/  # renomme index la fonction de views.index
    path('<int:book_id>',views.show, name = 'show')  #manga/<id>
]