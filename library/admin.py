from django.contrib import admin
from library.models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ('ISBN', 'title', 'description',
              'year_release')


