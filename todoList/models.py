from django.db import models
from django.conf import settings

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    task_title = models.CharField(max_length=100)
    task_text = models.CharField(max_length=2000)
    task_date = models.DateTimeField(null=True)
    task_status = models.BooleanField(null=True)

    def __str__(self):
        return self.task_text

    # date format: datetime(yyyy, m, d, h, m, s, ms, tzinfo=pytz.UTC)

