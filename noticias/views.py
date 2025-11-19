
from django.shortcuts import render, get_object_or_404
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

# Stripe - adicionar pagamento caminho inicial
def buscar(request):
    noticias = Noticia.objects.all()
    if "buscar" in request.GET:
        nome_buscar = request.GET["buscar"]
        if nome_buscar:
            busca_titulo = noticias.filter(titulo__icontains=nome_buscar)
            busca_conteudo = noticias.filter(conteudo__icontains=nome_buscar)
            noticias = busca_titulo | busca_conteudo

            noticias = noticias.distinct()
    return render(request, 'noticias/buscar.html',{'noticias': noticias})


def detalhe_noticia(request, noticia_id):
    noticia_principal = get_object_or_404(Noticia, pk=noticia_id)
    ultimas_noticias = Noticia.objects.exclude(pk=noticia_id).order_by('-data_publicacao')[:4]
    contexto = {
        'noticia': noticia_principal,
        'ultimas_noticias': ultimas_noticias
    }
    return render(request, 'noticias/detalhe_noticia.html', contexto)
