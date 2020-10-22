from django.urls import path
from library.views import AuthorEdit, AuthorList, create_author_many

app_name = 'library'
urlpatterns = [
    path('author/create', AuthorEdit.as_view(), name="author_create"),
    path('authors', AuthorList.as_view(), name="authors_list"),
    path('author/create_many', create_author_many, name="author_create_many"),
]
