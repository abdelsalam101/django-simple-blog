from django.contrib import admin
from .models import Post, Author, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('date', 'author', 'tags')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)