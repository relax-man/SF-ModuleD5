from django.urls import path
from library import views

app_name = 'library'
urlpatterns = [
    path('', views.home_page, name="home"),
    path('author/create/', views.AuthorEdit.as_view(), name="author_create"),
    path('authors/', views.AuthorList.as_view(), name="authors_list"),
    path('author/create_many/', views.create_author_many, name="author_create_many")
]
