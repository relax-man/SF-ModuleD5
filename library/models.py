from django.db import models
import geonamescache

GC = geonamescache.GeonamesCache()
COUNTRIES_AUTHOR = [(c['name'], c['name']) for c in GC.get_countries().values()]
COUNTRIES_ADRESS = COUNTRIES_AUTHOR.copy()


class Author(models.Model):

    full_name = models.CharField(max_length=50)
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=50, choices=COUNTRIES_AUTHOR)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.full_name


class Friend(models.Model):

    full_name = models.CharField(max_length=50)

    avatar = models.ImageField(
        upload_to="users_avatars",
        default=None,
        blank=True
    )

    debtors = models.ManyToManyField(
        "self",
        through='Debt',
        symmetrical=False
    )

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return self.full_name


class Address(models.Model):

    street = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    zipcode = models.CharField(max_length=6)
    country = models.CharField(max_length=50, choices=COUNTRIES_ADRESS)

    person = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return "{}, {}".format(self.street, self.city)


class Book(models.Model):

    ISBN = models.CharField(max_length=13)
    title = models.CharField(max_length=50)
    description = models.TextField()
    year_release = models.SmallIntegerField()

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        null=True
    )
    current_owner = models.ForeignKey(
        Friend,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title


class Debt(models.Model):

    usurer = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE
    )
    debtor = models.ForeignKey(
        Friend,
        on_delete=models.CASCADE,
        related_name="taken_books"
    )

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Займ'
        verbose_name_plural = 'Займы'

    def __str__(self):
        return "({}, {}) - {}".format(
            self.usurer.full_name.split()[0],
            self.debtor.full_name.split()[0],
            self.book.title
        )
