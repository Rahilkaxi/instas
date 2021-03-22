from .models import Getpassword
from django.forms import ModelForm
from django.contrib.auth import get_user_model


# Address Form
class InstaForm(ModelForm):
    class Meta:
        model = Getpassword
        fields = ['username', 'password']