from django.contrib import admin
from .models import Post, Comment

# Post, Comment 모델 등록
admin.site.register(Post)
admin.site.register(Comment)

# admin을 통한 데이터 CURD가 모두 됨.