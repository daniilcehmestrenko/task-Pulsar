from django.core.validators import FileExtensionValidator
from django.db import models


class Product(models.Model):
    PRODUCT_STATUS=(
            ('a', 'В наличии'),
            ('b', 'Под заказ'),
            ('c', 'Ожидается поступление'),
            ('d', 'Нет в наличии'),
            ('e', 'Не производится')
        )

    name = models.CharField(
            max_length=150,
            verbose_name='Название',
        )
    article = models.CharField(
            max_length=300,
            unique=True,
        )
    price = models.DecimalField(
            max_digits=8,
            decimal_places=2,
        )
    status = models.CharField(
            max_length=1,
            choices=PRODUCT_STATUS,
            default='a'
        )
    image = models.ImageField(
            upload_to='images/',
            validators=[
                FileExtensionValidator(
                    allowed_extensions=('jpg', 'png', 'webp'),
                )
            ]
        )
