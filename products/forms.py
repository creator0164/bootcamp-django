from django import forms
from django.forms import fields
from .models import Product

# class ProductForm(forms.Form):
#    title = forms.CharField()


class ProductForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
        ]

    def clean_content(self):
        data = self.cleaned_data.get('content')
        data_content = self.cleaned_data.get('content')
        if len(data) < 4:
            raise forms.ValidationError('This is not long enough.')
        return data
