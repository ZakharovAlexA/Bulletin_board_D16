from django.contrib.auth.models import User
from django.core.mail import send_mail


def mail_response_created(instanse, **kwargs):
    send_mail(
        subject='На ваше объявление пришёл отклик!',
        message=f'{instanse.article.author.username}, вам отклик от {instanse.responseAuthor}!',
        from_email=None,
        recipient_list=[instanse.article.author.email]
    )


def mail_response_accept(instanse, **kwargs):
    send_mail(
        subject='Ваш отклик принят!',
        message=f'{instanse.responseAuthor.username}, ваш отклик к "{instanse.article.title}" принят',
        from_email=None,
        recipient_list=[instanse.responseAuthor.email]
    )


def mail_news_created(instanse, **kwargs):
    send_mail(
        subject='Новость с Доски Объявлений MMORPG',
        message=f'Новость: {instanse.title} ПОДРОБНОСТИ: {instanse.text}!',
        from_email=None,
        recipient_list=[User.objects.filter(is_active=True).values_list('email', flat=True)]
    )
