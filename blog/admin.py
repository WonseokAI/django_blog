from django.contrib import admin
from blog.models import Category, Post

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'createDate', 'updateDate']
    list_filter = ['category']
    search_fields = ['title']
    ordering = ['-createDate', '-updateDate']


admin.site.register(Post, PostAdmin)
