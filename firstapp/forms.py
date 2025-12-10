from django import forms
from .models import Book
# class BookForm(forms.Form):

#     title = forms.CharField(label='Title', max_length=50)
#     author = forms.CharField(label='Author', max_length=50)
#     price = forms.IntegerField(label='Price')
#     publisher = forms.CharField(label='Publisher', max_length=50)
#     ebook = forms.BooleanField(label='E-Book', initial=True)


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'