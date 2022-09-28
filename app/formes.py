from django import forms
from .models import Post


class AddForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('add_email', 'comment')
