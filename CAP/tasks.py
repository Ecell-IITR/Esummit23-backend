from celery import shared_task


@shared_task()
def delete_submission(usertaskid):
    pass
  #Submission.objects.filter(id=usertaskid).delete()