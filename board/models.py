from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Article(models.Model):
    CATEGORY_CHOICES = (
        ('tanks', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('dealers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('smithы', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potions', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES, default='tanks')
    upload = models.FileField(upload_to='uploads/', blank=True)
    dateCreation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('article', args=[str(self.id)])


class UserResponse(models.Model):
    responseAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)


class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('news', args=[str(self.id)])
