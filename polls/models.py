from django.db import models

# Create your models here.

class MoshinaModel(models.Model):
    Mijoz = models.CharField(default='', max_length=200)
    Dardi = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Mijoz
    

