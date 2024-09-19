from django.contrib import admin
from .models import Blog, Comment

# Blog modelini admin panelida ro'yxatdan o'tkazamiz
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)

# Comment modelini admin panelida ro'yxatdan o'tkazamiz
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'user', 'created_at')
    search_fields = ('blog__title', 'user__username')
    list_filter = ('created_at',)
 