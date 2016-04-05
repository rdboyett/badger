# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, DeleteView

from braces.views import LoginRequiredMixin

from .models import MyBadge, Badge, Category, Platform, Subject
from .forms import SearchForm


class SearchFormMixin(object):

    def get_context_data(self, **kwargs):
        context = super(SearchFormMixin, self).get_context_data(**kwargs)
        context['searchForm'] = SearchForm
        return context


class IndexListView(LoginRequiredMixin, SearchFormMixin, ListView):
    model = MyBadge
    select_related = ['badge']

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs)
        context['awarded'] = self.model.objects.awarded_badges(self.request.user)
        context['wanted'] = self.model.objects.wanted_badges(self.request.user)
        return context


class SearchListView(LoginRequiredMixin, SearchFormMixin, ListView):
    model = Badge
    template_name = 'badge_tracker/search_list.html'
    context_object_name = 'badges'

    def get_queryset(self):
        query = self.request.GET['search']
        return self.model.objects.search_badges(query)


class BadgeDetailView(LoginRequiredMixin, SearchFormMixin, DetailView):
    model = Badge


class BadgeListView(LoginRequiredMixin, SearchFormMixin, ListView):
    model = Badge

    def get_context_data(self, **kwargs):
        context = super(BadgeListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['platforms'] = Platform.objects.all()
        context['subjects'] = Subject.objects.all()
        return context