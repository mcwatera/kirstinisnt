from django.contrib import admin
from .models import Blogpost, BlogpostComment

# Register your models here.
admin.site.register(Blogpost)
admin.site.register(BlogpostComment)
