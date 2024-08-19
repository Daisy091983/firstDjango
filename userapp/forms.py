from django.forms import ModelForm


from .models import UserDetails

class UserForm(Modelform):
    class Meta:
        model=UserDetails