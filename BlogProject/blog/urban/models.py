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
    creation_date = models.DateField()

    author = models.ForeignKey(Author, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}\n{self.content}'


class Comment(models.Model):
    id = models.IntegerField(primary_key=True, null=False, unique=True)
    content = models.TextField(null=False)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content}'
