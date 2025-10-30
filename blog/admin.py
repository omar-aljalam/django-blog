from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")
    list_filter = ("author", "date", "tags")
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, postAdmin)
admin.site.register(Author)
admin.site.register(Tag)
