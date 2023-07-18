from django import forms
from .models import Article, UserResponse, News


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'category',
            'text',
            'upload',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = [
            'text'
        ]


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'text'
        ]
