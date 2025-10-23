from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # makes the slug field read-only in the admin interface
    prepopulated_fields = {"slug": ("title",)} # automatically fills the slug field based on the title field
    list_filter = ("rating", "author", "is_bestseller")
    list_display = ("title", "author", "rating", "is_bestseller")

admin.site.register(Book, BookAdmin)