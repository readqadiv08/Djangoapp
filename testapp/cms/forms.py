from django.forms import ModelForm
from cms.models import User


class UserForm(ModelForm):
    """Userのフォーム"""
    class Meta:
        model = User
        fields = ('name', 'sex', 'age', )