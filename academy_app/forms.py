from django import forms
# academy_app/forms.py
from .models import AcademyComment  # تغيير الاسم هنا


class CommentForm(forms.ModelForm):
    class Meta:
        model = AcademyComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'اكتب تعليقك هنا...'}),
        }

