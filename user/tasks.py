from django.core.mail import send_mail
from celery import shared_task
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from django.utils.html import strip_tags


@shared_task()
def send_feedback_email_task(email, message, subject):
    if type(email) == list:
        send_mail(subject,"",'from@example.com',
                  email, fail_silently=False, html_message=message)
    else:
        html_message = message
        msg = MIMEText(strip_tags(html_message), 'html', 'utf-8')
        send_mail(subject,"",'no.reply.esummit@gmail.com',
                  [email], fail_silently=False,html_message=html_message) 

@shared_task()
def send_link_email_task(queryset, User,desc):
 
        for query in queryset:
            email_address = query.Person.email
          
            mail_message= User

            mail_subject = desc
            send_feedback_email_task(email_address,mail_message,mail_subject)
