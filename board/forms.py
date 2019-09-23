from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
        'title': forms.Textarea(attrs={'class': 'post_create'}),
        'content': forms.Textarea(attrs={'class': 'post_create',
        'rows': 5,
        'cols': 50, 
            })
        }
        labels = {
            'title': '제목',
            'content': '내용',
            'image': '사진',
        }
        required = {
            'image':False,
        }
