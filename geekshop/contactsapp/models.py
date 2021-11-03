from django.db import models

# Create your models here.

class Contact(models.Model):
    city = models.CharField(
        max_length=64,
        verbose_name='город',
        unique=True,
    )

    address = models.TextField(
        verbose_name='адрес',
    )

    telephone = models.CharField(
        max_length=20,
        verbose_name='телефон',
    )

    email = models.CharField(
        max_length=128,
        verbose_name='email',
    )

    def __str__(self):
        return self.city