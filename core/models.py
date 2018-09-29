from django.db import models
from django.utils import timezone


class Post(models.Model):
    nome = models.CharField(max_length=50, null=False)
    titulo = models.CharField(max_length=200, null=False)
    texto = models.TextField(null=False)
    setor = models.CharField(max_length=50, null=False)

    data = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.data = timezone.now()
        self.save()
