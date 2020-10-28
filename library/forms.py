from django.forms.models import inlineformset_factory
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.forms import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML
from crispy_forms.layout import Row, Column, ButtonHolder, Submit
from crispy_forms.bootstrap import AppendedText

from django import forms
from library import models
from library.utils import Formset
import re


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

    def clean(self):
        cleaned_data = super(AuthorForm, self).clean()

        full_name = cleaned_data.get('full_name')
        if full_name:
            if len(full_name.split()) < 2:
                raise ValidationError(
                    {'full_name': 'Please, enter your full name.'}
                )

        birth_year = cleaned_data.get('birth_year')
        if birth_year:
            if birth_year < 1000 or birth_year > 2000:
                raise ValidationError(
                    {'birth_year': 'Incorrent birth year.'}
                )

        return cleaned_data


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = '__all__'

    def clean(self):
        cleaned_data = super(BookForm, self).clean()

        isbn = cleaned_data.get('isbn')
        if isbn:
            if not isbn.isdigit():
                raise ValidationError(
                    {'ISBN': 'ISBN should contain only digits.'}
                )
            if len(isbn) != 13:
                raise ValidationError(
                    {'ISBN': 'ISBN is too short.'}
                )

        year = cleaned_data.get('year_release')
        if year:
            if year < 1000 or year > 2020:
                raise ValidationError(
                    {'year_release': 'Incorrect release year.'}
                )

        return cleaned_data


class AddressForm(forms.ModelForm):

    class Meta:
        model = models.Address
        exclude = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        formtag_prefix = re.sub('-[0-9]+$', '', kwargs.get('prefix', ''))

        self.helper = FormHelper()
        self.helper.disable_csrf = True

        self.helper.layout = Layout(
            Row(
                Column(Field('street', placeholder='4586 Hillhaven Drive'),
                       css_class='col-12'),
                Column(Field('city', placeholder='Los Angeles'),
                       css_class='col-4'),
                Column(Field('country', placeholder='United States'),
                       css_class='col-4'),
                Column(Field('zipcode', placeholder='90071'),
                       css_class='col'),

                css_class='formset_row-{} mb-3'.format(formtag_prefix)
            )
        )

    def clean(self):
        cleaned_data = super(AddressForm, self).clean()

        zipcode = cleaned_data.get('zipcode')
        if zipcode:
            if not zipcode.isdigit():
                raise ValidationError(
                    {'zipcode': 'Zipcode should contain only digits.'}
                )
            elif len(zipcode) < 5:
                raise ValidationError(
                    {'zipcode': 'Zipcode is too short.'}
                )

        return cleaned_data


class FriendForm(forms.ModelForm):

    class Meta:
        model = models.Friend
        exclude = ['debtors']

    def __init__(self, *args, **kwargs):
        super(FriendForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontale needs-validation'
        self.helper.label_class = 'col-12'
        self.helper.field_class = 'col-12'

        self.helper.layout = Layout(
            Div(
                Row(
                    Column(Field('avatar', template='forms/image_field.html'),
                           css_class='col-6 col-md-3 pr-4 mb-2'),
                    Column(Field('full_name'),
                           css_class='col-6 col-md-9')
                ),
                Formset('addresses'),
                HTML('<hr>'),

                ButtonHolder(
                    Submit('submit', 'Save', formnovalidate='False',
                           css_class='col col-md-3 btn-success ml-md-auto'),

                    css_class='d-flex'
                )
            )
        )

    def clean(self):
        cleaned_data = super(FriendForm, self).clean()

        full_name = cleaned_data.get('full_name')
        if full_name and len(full_name.split()) < 2:
            raise ValidationError(
                {'full_name': 'Please, enter your full name.'}
            )

        return cleaned_data


AddressFormSet = inlineformset_factory(
    models.Friend,
    models.Address,
    form=AddressForm,
    exclude=['person'],
    extra=0,
    can_delete=True,
    min_num=1,
    max_num=3
)
