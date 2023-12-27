from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

# admin을 통한 데이터 CURD가 모두 됨.