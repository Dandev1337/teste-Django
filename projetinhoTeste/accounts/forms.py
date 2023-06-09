from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["first_name", "username", "email"]
