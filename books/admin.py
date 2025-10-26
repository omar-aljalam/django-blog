from django.contrib import admin

from .models import Book, Author, Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",) # makes the slug field read-only in the admin interface
    prepopulated_fields = {"slug": ("title",)} # automatically fills the slug field based on the title field
    list_filter = ("title", "rating", "author", "is_bestseller")
    list_display = ("title", "rating", "author", "is_bestseller")

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)