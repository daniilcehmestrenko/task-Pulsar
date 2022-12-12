from PIL import Image
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
            verbose_name='Артикул'
        )
    price = models.DecimalField(
            max_digits=8,
            decimal_places=2,
            verbose_name='Цена'
        )
    status = models.CharField(
            max_length=1,
            choices=PRODUCT_STATUS,
            default='a',
            verbose_name='Статус'
        )
    image = models.ImageField(
            upload_to='images/',
            validators=[
                FileExtensionValidator(
                    allowed_extensions=('jpg', 'png', 'webp'),
                )
            ],
            verbose_name='Картинка'
        )
    
    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        if self.image:
            filename = self.image.path
            image = Image.open(filename)
            image = image.convert('RGB')
            image.save(filename)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
