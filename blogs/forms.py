from django import forms 
from ckeditor.widgets import CKEditorWidget
from .models import *


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'cover_image', 'content']
        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Article Title'}),
                'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }
    content = forms.CharField(widget=CKEditorWidget())