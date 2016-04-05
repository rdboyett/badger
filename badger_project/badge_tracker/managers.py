from __future__ import unicode_literals

from django.db import models

from .utils import QuerySetChain


class BadgeManager(models.Manager):

    def search_badges(self, criteria):
        title = self.filter(title__icontains=criteria)
        titleList = title.values_list('id', flat=True)
        description = self.filter(description__icontains=criteria).exclude(id__in=titleList)  # prevent duplicate badges
        return QuerySetChain(title, description)


class MyBadgeManager(models.Manager):

    use_for_related_fields = True

    def awarded_badges(self, user):
        return self.select_related('badge').filter(user=user, awarded=True)

    def wanted_badges(self, user):
        return self.select_related('badge').filter(user=user, awarded=False)

