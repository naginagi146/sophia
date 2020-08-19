from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'is_public', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    list_filter = ('title','is_public',)
    search_fields = ('title', 'text')



admin.site.register(Post, PostAdmin)

# Register your models here.
