from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel, ActivatorModel, TitleSlugDescriptionModel, TitleDescriptionModel

from .managers import BadgeManager, MyBadgeManager


def get_image_name(instance, filename):
    return 'badges/image.png'

class Category(TitleSlugDescriptionModel, models.Model):
    order = models.IntegerField(default=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order','title']

class Platform(TitleSlugDescriptionModel, models.Model):
    order = models.IntegerField(default=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order','title']


class Subject(TitleSlugDescriptionModel, models.Model):
    order = models.IntegerField(default=10)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order','title']


class Criteria(TitleDescriptionModel, models.Model):
    def __str__(self):
        return self.title


class Display(TimeStampedModel, models.Model):
    type = models.CharField(max_length=10, choices=(('image','image'),('video','video')), default='image')
    uploadedResource = models.ImageField(upload_to="display_uploads", blank=True, null=True, verbose_name="Uploaded Resource")
    linkedResource = models.URLField(blank=True, verbose_name="Linked Resource")

    def __str__(self):
        return self.type


class Badge(TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel, models.Model):
    """
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), blank=True, null=True)
    slug = AutoSlugField(_('slug'), populate_from='title')
    created = CreationDateTimeField(_('created'))
    modified = ModificationDateTimeField(_('modified'))
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=ACTIVE_STATUS)
    activate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for an immediate activation'))
    deactivate_date = models.DateTimeField(blank=True, null=True, help_text=_('keep empty for indefinite activation'))
    """
    image = models.URLField(verbose_name="Image Link")
    destinationLink = models.URLField(blank=True)
    displays = models.ManyToManyField(Display, blank=True)
    categories = models.ManyToManyField(Category)
    platforms = models.ManyToManyField(Platform)
    subjects = models.ManyToManyField(Subject)
    criteria = models.ForeignKey(Criteria, blank=True, null=True)
    popularity = models.IntegerField(default=0)

    objects = BadgeManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('badge:detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-popularity', 'title', 'modified']


class MyBadge(TimeStampedModel, models.Model):
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    awarded = models.BooleanField(default=False)

    objects = MyBadgeManager()

    def __str__(self):
        return self.badge.title



admin.site.register(Category)
admin.site.register(Platform)
admin.site.register(Subject)
admin.site.register(Badge)
admin.site.register(MyBadge)
admin.site.register(Criteria)