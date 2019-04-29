from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)
    company_url = models.CharField(max_length=200, null=True, blank=True)
    posting_url = models.CharField(max_length=200, null=True, blank=True)
    portal_url = models.CharField(max_length=200, null=True, blank=True)
    portal_login = models.CharField(max_length=50, null=True, blank=True)
    portal_pass = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    posted_on = models.DateField(null=True, blank=True)
    closes_on = models.DateField(null=True, blank=True)
    applied_on = models.DateField(null=True, blank=True)
    resume = models.FileField(upload_to='user/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='user/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_stale = models.BooleanField(default=False)

    def __str__(self):
        return (self.position + ' @ ' + self.company)
