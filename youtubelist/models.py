from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=250)
    url = models.URLField()
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo