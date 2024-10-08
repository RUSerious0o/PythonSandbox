from django.db import models


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=32)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.balance}, {self.age}'


class Game(models.Model):
    title = models.CharField(max_length=128)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.DecimalField(max_digits=14, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')

    def __str__(self):
        return f'{self.title} | {self.description}. Стоимость: {self.cost} '
