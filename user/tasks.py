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
def send_link_email_task(queryset, User,desc):
 
        for query in queryset:
            email_address = query.Person.email
          
            mail_message= User

            mail_subject = desc
            send_feedback_email_task(email_address,mail_message,mail_subject)
