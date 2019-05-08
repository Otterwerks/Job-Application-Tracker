import os, datetime
from django.db import models
from applications.models import Application

def get_upload_path(instance, filename):
    return os.path.join("user_%d" % instance.owner.id, "company_%s" % instance.slug, filename)


class Event(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, default="Note")
    event_text = models.TextField(null=True, blank=True)
    event_date = models.DateField(default = datetime.date.today)

    def __str__(self):
        return (self.event_type + ' on ' + self.event_date)

