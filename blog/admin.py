from blog.models import Author, Post, Tag, Comment
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=("title","author")
    list_filter=("author","title","tag",)

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")
    
# Register your models here.

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)