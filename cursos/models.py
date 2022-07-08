from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
             # herança
class Curso(models.Model):
    nome = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=256, unique=True, null=True, blank=True)
    descricao = models.TextField()
    autor = models.CharField(max_length=128, default="EU", null=True, blank=True)
    ativo = models.BooleanField(default=True)
    imagem = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.nome)
        super(Curso, self).save(*args, **kwargs)

class Aula(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.TextField()
    duracao = models.DurationField()
    video_url = models.URLField()