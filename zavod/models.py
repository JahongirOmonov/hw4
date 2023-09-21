from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Mashinalar(AbstractUser):
    MoshinaTurlari = (
        (3,'Nexia'),
        (2, 'Matiz'),
        (1, 'Tico')
    )

    roles = models.PositiveIntegerField(choices=MoshinaTurlari, default=1)
