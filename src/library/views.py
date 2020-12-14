from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

from django.views.generic import ListView, CreateView
from .utils import ObjectListMixin, ObjectCreateMixin
from .forms import AuthorForm, BookForm, FriendForm, AddressFormSet
from .models import Author, Book, Friend

from django.db import transaction


def home_page(request):
    home_data = {
        'title': 'Library'
    }
    return render(request, 'index.html', home_data)


class AuthorList(ObjectListMixin, ListView):
    model = Author
    template_name = 'author/author_list.html'


class BookList(ObjectListMixin, ListView):
    model = Book
    template_name = 'book/book_list.html'
    ordering = '-year_release'


class FriendList(ObjectListMixin, ListView):
    model = Friend
    template_name = 'friend/friend_list.html'


class AuthorCreate(ObjectCreateMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'author/author_edit.html'
    success_url = reverse_lazy('library:author_list')


class BookCreate(ObjectCreateMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'author/author_edit.html'
    success_url = reverse_lazy('library:book_list')


class FriendCreate(ObjectCreateMixin, CreateView):
    model = Friend
    form_class = FriendForm
    template_name = 'friend/friend_edit.html'
    success_url = reverse_lazy('library:friend_list')


    def get_context_data(self, **kwargs):
        data = super(FriendCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['addresses'] = AddressFormSet(self.request.POST)
        else:
            data['addresses'] = AddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        addresses = context['addresses']

        with transaction.atomic():
            form.instance.created_by = self.request.user

            if not form.is_valid() or not addresses.is_valid():
                return self.form_invalid(form)

            self.object = form.save()
            addresses.instance = self.object
            addresses.save()

        return super(FriendCreate, self).form_valid(form)
