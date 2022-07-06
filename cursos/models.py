from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=128)
    descrição = models.TextField()
    autor = models.CharField(max_length=128, default="EU", null=True)
    ativo = models.BooleanField(default=True)
