from django.urls import path
from library import views

app_name = 'library'
urlpatterns = [
    path(
        '',
        views.home_page,
        name="home"
    ),
    path(
        'author/',
        views.AuthorList.as_view(),
        name="author_list"
    ),
    path(
        'author/create/',
        views.AuthorCreate.as_view(),
        name="author_create"
    ),
    path(
        'book/',
        views.BookList.as_view(),
        name="book_list"
    ),
    path(
        'book/create/',
        views.BookCreate.as_view(),
        name="book_create"
    ),
    path(
        'friend/',
        views.FriendList.as_view(),
        name="friend_list"
    ),
    path(
        'friend/create/',
        views.FriendCreate.as_view(),
        name="friend_create"
    )
]
