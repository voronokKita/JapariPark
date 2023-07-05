"""Django's admin configurations for the Friends app."""
from django.contrib import admin

from .models import TestEntry, TestPost


@admin.register(TestEntry)
class TestEntryAdmin(admin.ModelAdmin):
    """Admin view for TestEntry."""

    list_display = ['pk', 'text', 'pub_date']
    list_display_links = ['pk', 'text']
    list_filter = ['pub_date']

    ordering = ['-pub_date']

    fields = ['text']
    search_fields = ['text']


@admin.register(TestPost)
class TestPostAdmin(admin.ModelAdmin):
    """Admin view for TestPost."""

    list_display = ['pk', 'text', 'pub_date']
    list_display_links = ['pk', 'text']
    list_filter = ['pub_date']

    ordering = ['-pub_date']

    fields = ['text']
    search_fields = ['text']
