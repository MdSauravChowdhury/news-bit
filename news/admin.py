from django.contrib import admin
from .models import Author, category, Post, EmailSubcribe

#Register your models here.
admin.site.register(Author)
admin.site.register(category)
admin.site.register(Post)
admin.site.register(EmailSubcribe)