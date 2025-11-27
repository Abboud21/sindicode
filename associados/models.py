from django.db import models

class Associado(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('B', 'Binário'),
        ('O', 'Outros'),
        ('N', 'Prefiro não responder'),
    ]

    cpf = models.CharField(max_length=14, unique=True)  # formato XXX.XXX.XXX-XX
    rg = models.CharField(max_length=20)
    nome_completo = models.CharField(max_length=150)
    nome_social = models.CharField(max_length=150, blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.nome_completo} ({self.cpf})"
