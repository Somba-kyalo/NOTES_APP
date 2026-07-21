from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_filter = ("created_at", "updated_at")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Note Information", {"fields": ("title", "content")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )