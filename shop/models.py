from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30, default='')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}-{self.price}'


class Purchase(models.Model):
    name = models.CharField(max_length=30, default='')
    age = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_purchase = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'{self.name}-{self.age}-{self.item.name}{self.item.price}'
