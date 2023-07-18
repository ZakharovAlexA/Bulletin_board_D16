from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import mail_response_created, mail_response_accept, mail_news_created

from .models import UserResponse, News


@receiver(post_save, sender=UserResponse)
def response_created(instance, created, **kwargs):
    if created:
        mail_response_created(instance)


@receiver(post_save, sender=UserResponse)
def response_accept(instance, **kwargs):
    if instance.status:
        mail_response_accept(instance)


@receiver(post_save, sender=News)
def news_created(instance, created, **kwargs):
    if created:
        mail_news_created(instance)
