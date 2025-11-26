
from django.db import models, transaction


# estudar ORM (object-relation-mapper)
class Categoria(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    def __str__(self):
        return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    perfil = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.nome+self.perfil

class Noticia(models.Model):
    titulo = models.CharField(max_length=90, null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)
    data_publicacao = models.DateTimeField(null=False, blank=False, auto_now=True)
    destaque = models.CharField(max_length=5 , choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4')], default='4')
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=False)
    #Relacionamento N-1(Muitas Noticias para um Autor)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='noticias_autor', null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='noticias_categoria', null=False)
    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if self.destaque in ['0', '1', '2', '3']:
            # Convertemos para inteiro para poder fazer contas (loop)
            destaque_nivel = int(self.destaque)
            with transaction.atomic():
                # O Loop Mágico: Vamos do 3 descendo até o nível que inserimos.
                for i in range(3, destaque_nivel - 1, -1):
                    # Filtra as notícias do nível atual 'i'
                    # .exclude(pk=self.pk) impede que mexamos na notícia que estamos salvando agora (caso seja edição)
                    qs = Noticia.objects.filter(destaque=str(i)).exclude(pk=self.pk)
                    # Atualiza elas para o nível logo abaixo (i + 1)
                    qs.update(destaque=str(i + 1))
        super().save(*args, **kwargs)
# Create your models here.
#python manage.py makemigrations
#python manage.py migrate
