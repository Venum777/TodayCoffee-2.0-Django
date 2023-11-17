# Python
import random

# Django
from django.conf import settings
from django.core.mail import EmailMessage


def send_email(
    subject: str,
    body: str,
    to_emails: list[str]
) -> None:
    email = EmailMessage(
        subject,
        body,
        settings.EMAIL_FROM,
        to_emails
    )
    email.send()

def generate_string() -> str:
    simbols: str = (
        'qwertyuiop'
        'asdfghjkl'
        'zxcvbnm'
        '1234567890'
        '!@#$%*+'
    )
    code: str = ''
    _: int
    for _ in range(20):
        code += random.choice(simbols)

    return code
