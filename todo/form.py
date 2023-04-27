from django.forms import ModelForm
from .models import TodoL

class CreateTask(ModelForm):
    class Meta:
        model = TodoL
        fields = "__all__"
        exclude = ["user"]