from django.shortcuts import render
from django.http import HttpResponse

from noticias.models import Categoria, Autor, Noticia


# função
# se def dentro classe = metodo
# se def fora classe = funçao
def index(request):
    #return HttpResponse("<h1>Alô Django 2005</h1>")
    #definindo um mock com dict (dicionário python)
    # dados ={
    #     1:{"titulo":"mulheres dev","conteudo":"mulheres programadores em python","data_publicacao":"29/10/2025"},
    #     2:{"titulo":"programadores kids","conteudo":"programadores em python no dia das crianças","data_publicacao":"12/10/2025"},
    #     3:{"titulo":"Josias novo presidente","conteudo":"Josias é nosso novo presidente","data_publicacao":"06/06/2006"},
    # }
    categorias = Categoria.objects.all()
    return render(request, 'noticias/index.html', {'cards': categorias})

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/index.html', {'noticias': noticias})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'noticias/nossos-autores.html', {'autores': autores})

