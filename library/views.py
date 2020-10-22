from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render

from django.views.generic import CreateView, ListView
from django.forms import formset_factory
from library.forms import AuthorForm
from library.models import Author


def home_page(request):
    home_data = {
        'title': 'Library'
    }
    return render(request, 'index.html', home_data)

class AuthorEdit(CreateView):
    model = Author
    form_class = AuthorForm
    success_url = reverse_lazy('library:author_create')
    template_name = 'author_edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Book create'
        return context

class AuthorList(ListView):
    model = Author
    template_name = 'author_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Books list'
        return context


def create_author_many(request):
    AuthorFormSet = formset_factory(AuthorForm, extra=2)

    if request.method == "POST":
        author_formset = AuthorFormSet(request.POST, request.FILES, prefix='authors')

        if author_formset.is_valid():
            for author_form in author_formset:
                author_form.save()
            return HttpResponseRedirect(reverse_lazy('library:authors_list'))

    else:
        author_formset = AuthorFormSet(prefix='authors')

    return render(request, 'manage_authors.html', {'author_formset': author_formset})
