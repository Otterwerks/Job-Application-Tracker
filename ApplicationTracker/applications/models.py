from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=50, blank=True)
    company_url = models.CharField(max_length=200, blank=True)
    posting_url = models.CharField(max_length=200, blank=True)
    portal_url = models.CharField(max_length=200, blank=True)
    portal_login = models.CharField(max_length=50, blank=True)
    portal_pass = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=50, blank=True)
    body = models.TextField(blank=True)
    posted_on = models.DateField(blank=True)
    closes_on = models.DateField(blank=True)
    applied_on = models.DateField(blank=True)
    resume = models.FileField(upload_to='user/', blank=True)
    cover_letter = models.FileField(upload_to='user/', blank=True)
    is_active = models.BooleanField(default=True)
    is_stale = models.BooleanField(default=False)

    def __str__(self):
        return (self.position + ' @ ' + self.company)
