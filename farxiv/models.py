from django.db import models
from django.contrib.auth.models import User

class Field(models.Model):
    name        = models.TextField(max_length=512)

class Topic(models.Model):
    name        = models.TextField(max_length=512)
    field       = models.ForeignKey(Field)

class Profile(models.Model):
    user        = models.ForeignKey(User)
    fields      = models.ManyToManyField(Field)

class FailureReasons(models.Model):
    reason_text = models.TextField(max_length=1024)
    extended_reason = models.TextField()
    def __str__(self):
        return self.reason_text

class Keyword(models.Model):
    keyword     = models.TextField(max_length=256)

class Farticle(models.Model):
    author      = models.ForeignKey(User)
    topic       = models.ForeignKey(Topic)
    title       = models.TextField(max_length=1024)
    farticle    = models.FileField()
    failure_reasons = models.ManyToManyField(FailureReasons)
    keywords    = models.ManyToManyField(Keyword)
    submitted_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
