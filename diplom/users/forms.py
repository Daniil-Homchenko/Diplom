from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()

class UserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label=_("First_name"),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    ),
    last_name = forms.CharField(
        label=_("Last_name"),
        widget=forms.TextInput(attrs={'class': 'form-input'})
    ),
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'last_name', 'first_name')