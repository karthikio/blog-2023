from django.contrib import admin
from .models import Post, Tag, Feedback


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Feedback)


admin.site.site_header = "BlogApp Admin"
admin.site.site_title = "Blog app"
