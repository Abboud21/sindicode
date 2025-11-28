from django.db import models

class Associado(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20)
    nome_completo = models.CharField(max_length=200)
    nome_social = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.nome_completo


class Endereco(models.Model):
    associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}"


class Contato(models.Model):
    associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.email or "Contato"


class SituacaoAssociado(models.Model):
    associado = models.ForeignKey(Associado, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    observacao = models.TextField(blank=True, null=True)
    data_status = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.associado.nome_completo} - {self.status}"
