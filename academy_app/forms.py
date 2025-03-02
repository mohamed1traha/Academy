from django import forms
# academy_app/forms.py
from .models import AcademyComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = AcademyComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

