from django.db import models


class Author(models.Model):

    full_name = models.CharField(max_length=50)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Book(models.Model):

    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=128)
    description = models.TextField()
    year_release = models.SmallIntegerField()

    author = models.ManyToManyField(
        Author,
        through='Inspiration',
        through_fields=('book', 'author')
    )

    def __str__(self):
        return self.title


class Inspiration(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    inspirer = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='inspired_works'
    )



