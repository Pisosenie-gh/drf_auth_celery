from drf_auth_with_celery.celery import app
from django.core.mail import send_mail
from drf_auth_with_celery.settings import EMAIL_HOST


@app.task
def send_register_email(user_email):
    send_mail(
        'Registration successful',
        'THX',
        f'{EMAIL_HOST}',
        [user_email],
        fail_silently=False
    )

