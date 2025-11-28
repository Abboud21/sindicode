
from django.shortcuts import render
from .models import Associado


def associados(request):
    lista = Associado.objects.all().order_by('-id')  # pegar todos

    return render(request, 'associados/index.html', {
        'associados': lista
    })

def login(request):
    return render(request, 'associados/login.html')

def cadastro(request):
    nome = request.GET.get("nome", "")
    email = request.GET.get("email", "")

    if request.method == "POST":
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg")
        nome_completo = request.POST.get("nome_completo")
        nome_social = request.POST.get("nome_social")
        genero = request.POST.get("genero")
        data_nascimento_str = request.POST.get("data_nascimento")
        email_post = request.POST.get("email")

        # Converter para objeto date
        data_nascimento = None
        if data_nascimento_str:
            data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()

        Associado.objects.create(
            cpf=cpf,
            rg=rg,
            nome_completo=nome_completo,
            nome_social=nome_social,
            genero=genero,
            data_nascimento=data_nascimento,
            email = email_post
        )

        return redirect("associados")

    return render(request, "associados/cadastro.html", {
        "nome": nome,
        "email": email,
    })


def editar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)

    if request.method == "POST":
        associado.cpf = request.POST.get("cpf")
        associado.rg = request.POST.get("rg")
        associado.nome_completo = request.POST.get("nome_completo")
        associado.nome_social = request.POST.get("nome_social")
        associado.genero = request.POST.get("genero")
        associado.data_nascimento = request.POST.get("data_nascimento")
        associado.save()

        return redirect('associados')

    return render(request, 'associados/editar.html', {
        'associado': associado
    })


def deletar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    associado.delete()
    return redirect('associados')