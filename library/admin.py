from django.contrib import admin
from .models import *

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    pass