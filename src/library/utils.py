from crispy_forms.layout import LayoutObject, TEMPLATE_PACK
from django.template.loader import render_to_string
from django.urls import reverse_lazy

from .models import *


class ObjectListMixin:

    data = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standart_data = {
            'title': self.model.__name__.lower() + 's',
            'model': self.model.__name__.lower()
        }
        context.update(standart_data)
        context.update(self.data)
        return context


class ObjectCreateMixin:

    data = {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        standart_data = {
            'title': self.model.__name__.lower() + 's',
            'model': self.model.__name__.lower(),
            'success_url': self.success_url
        }
        context.update(standart_data)
        context.update(self.data)
        return context


class Formset(LayoutObject):

    template = "forms/formset.html"

    def __init__(self, formset_name, template=None):
        self.formset_name = formset_name
        if template:
            self.template = template

    def render(self, form, form_style, context, template_pack=TEMPLATE_PACK):
        formset = context[self.formset_name]
        return render_to_string(self.template, {'formset': formset})