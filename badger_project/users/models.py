# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TitleDescriptionModel

from badger_project.badge_tracker.models import Subject, MyBadge


SUBJECT_CHOICES = (
    ("All Subjects","All Subjects"),
    ("No Subjects","No Subjects"),
    ("English-Reading","English-Reading"),
    ("Math","Math"),
    ("Science","Science"),
    ("Social Studies","Social Studies"),
    ("Special Education","Special Education"),
    ("Language Studies","Language Studies"),
    ("CATE","Career and Technology Education")
)

SCHOOL_CHOICES = (
    ("none", 'None'),
    ('LES', 'Lillian Elementary'),
    ('AES', 'Elementary South'),
    ('AEN', 'Elementary North'),
    ('AIS', 'Intermediate'),
    ('AJH', 'Junior High'),
    ('AHS', 'High School'),
    ('Administration', 'Administration'),
    ('Operations', 'Operations'),
    ('Special Services', 'Special Services'),
    ('Technology', 'Technology'),
)

GRADE_CHOICES = (
    ("none","None"),
    ("K","Kindergarten"),
    ("1","1st"),
    ("2","2nd"),
    ("3","3rd"),
    ("4","4th"),
    ("5","5th"),
    ("6","6th"),
    ("7","7th"),
    ("8","8th"),
    ("9","9th"),
    ("10","10th"),
    ("11","11th"),
    ("12","12th"),
)

class Campus(TitleDescriptionModel, models.Model):
    def __str__(self):
        return self.title


class Grade(TitleDescriptionModel, models.Model):
    def __str__(self):
        return self.title



@python_2_unicode_compatible
class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    campus = models.ManyToManyField(Campus, blank=True)
    grade = models.ManyToManyField(Grade, blank=True)
    job = models.CharField(max_length=85, verbose_name='Occupation', default="Teacher")
    subject = models.ManyToManyField(Subject, blank=True)
    roomNumber = models.CharField(max_length=8, blank=True)
    phoneExtension = models.IntegerField(default=0)
    badges = models.ManyToManyField(MyBadge, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})



admin.site.register(Campus)
admin.site.register(Grade)