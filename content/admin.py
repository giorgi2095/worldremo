from django.contrib import admin

from content.models import Image, Post

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image

class PostAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Post, PostAdmin)