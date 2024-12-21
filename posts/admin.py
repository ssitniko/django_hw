from django.contrib import admin
from posts.models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'rate', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description') 
    list_display_links = ('title', 'description', 'created_at', 'updated_at')
    list_editable = ('rate',)

admin.site.register(Category)
admin.site.register(Tag)



# 1-ый вариант регистрации
# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(Tag)