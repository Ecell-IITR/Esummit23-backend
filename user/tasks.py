
from django.core.mail import send_mail
from celery import shared_task


@shared_task()
def send_feedback_email_task(email, message, subject):
    if type(email) == list:
        send_mail(subject, "", 'from@example.com',
                  email, fail_silently=False, html_message=message)
    else:
        send_mail(subject, "", 'from@example.com',
                  [email], fail_silently=False, html_message=message)
