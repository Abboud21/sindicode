from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Associado

# Página de associados (protegida)
def associados(request):
    if 'associado_id' not in request.session:
        return redirect('login')

    lista = Associado.objects.all().order_by('nome_completo')

    return render(request, 'associados/index.html', {
        'associados': lista,
        'nome_logado': request.session.get('associado_nome')
    })


# Cadastro de associado
def cadastro(request):
    nome = request.GET.get("nome", "")
    email = request.GET.get("email", "")

    if request.method == "POST":
        cpf = request.POST.get("cpf")
        rg = request.POST.get("rg")
        nome_completo = request.POST.get("nome_completo")
        genero = request.POST.get("genero")
        data_nascimento_str = request.POST.get("data_nascimento")
        email_post = request.POST.get("email")
        senha = request.POST.get("senha")
        senha_confirm = request.POST.get("senha_confirm")

        # Verificar se as senhas coincidem
        if senha != senha_confirm:
            return render(request, "associados/cadastro.html", {
                "erro": "As senhas não coincidem.",
                "nome": nome_completo,
                "email": email_post
            })

        # Converter para date
        data_nascimento = None
        if data_nascimento_str:
            data_nascimento = datetime.strptime(data_nascimento_str, "%Y-%m-%d").date()

        # Criar associado
        associado = Associado(
            cpf=cpf,
            rg=rg,
            nome_completo=nome_completo,
            genero=genero,
            data_nascimento=data_nascimento,
            email=email_post
        )

        associado.definir_senha(senha)
        associado.save()

        return redirect("login")

    return render(request, "associados/cadastro.html", {
        "nome": nome,
        "email": email,
    })


# Login de associado
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        try:
            associado = Associado.objects.get(email=email)

            if associado.verificar_senha(senha):
                request.session['associado_id'] = associado.id
                request.session['associado_nome'] = associado.nome_completo
                return redirect('associados')
            else:
                return render(request, 'associados/login.html', {
                    'erro': 'Senha incorreta.'
                })
        except Associado.DoesNotExist:
            return render(request, 'associados/login.html', {
                'erro': 'E-mail não cadastrado.'
            })

    return render(request, 'associados/login.html')


# Logout
def logout(request):
    request.session.flush()
    return redirect('login')


# Editar associado
def editar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)

    if request.method == "POST":
        associado.cpf = request.POST.get("cpf")
        associado.rg = request.POST.get("rg")
        associado.nome_completo = request.POST.get("nome_completo")
        associado.genero = request.POST.get("genero")
        associado.data_nascimento = request.POST.get("data_nascimento")
        associado.save()

        return redirect('associados')

    return render(request, 'associados/editar.html', {'associado': associado})


# Deletar associado
def deletar_associado(request, id):
    associado = get_object_or_404(Associado, id=id)
    associado.delete()
    return redirect('associados')
