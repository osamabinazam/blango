from django.contrib import admin
from blog.models import Post, Tag
# Customizing Model's information on admin panel
class PostAdmin(admin.ModelAdmin):
  list_display = ('slug', 'published_at')
  prepopulated_fields = {'slug' : ("title",)}



# Register your models here.
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
