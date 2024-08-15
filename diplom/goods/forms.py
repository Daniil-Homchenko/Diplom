from django import forms
from .models import Goods


class GoodForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['title', 'description', 'state', 'image', 'price', 'first_name', 'last_name', 'phone_number']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(GoodForm, self).__init__(*args, **kwargs)
        self.fields['state'].empty_label = 'Категория не выбрана'
        if user and user.is_authenticated:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name