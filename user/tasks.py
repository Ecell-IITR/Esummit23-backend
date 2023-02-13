from django.core.mail import send_mail
from celery import shared_task
from django.core.mail import EmailMessage


@shared_task()
def send_feedback_email_task(email, message, subject):
    if type(email) == list:
        send_mail(subject, "", 'from@example.com',
                  email, fail_silently=False, html_message=message)
    else:
        send_mail(subject, "", 'from@example.com',
                  [email], fail_silently=False, html_message=message)

@shared_task()
def send_link_email_task(email, message,subject, attachment):
 
        mail = EmailMessage(subject, message, "no.reply.esummit@gmail.com", [email])
        for f in attachment:
          mail.attach(f.name, f.read(), f.content_type)
        mail.send()
