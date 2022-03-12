from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=122)
    subtitle = models.CharField(max_length=122)
    author = models.CharField(max_length=56)
    isbn = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.title
