from django.db import models

# Create your models here.
class ProductsCategory(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='имя',
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='имя продукта',
    )

    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )

    category = models.ForeignKey(
        ProductsCategory,
        on_delete=models.CASCADE,
    )

    short_desc = models.CharField(
        max_length=60,
        verbose_name='краткое описание',
        blank=True,
    )

    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='цена',
    )

    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'



