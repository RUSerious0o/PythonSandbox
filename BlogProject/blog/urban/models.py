from django.db import models


# Create your models here.
class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=256, unique=True, null=False)
    content = models.TextField()

    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}\n{self.content}'
