from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Post(models.Model):
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True) # 생성이 되면 자동으로 입력해주는 속성
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    
class Comment(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE) # Post랑 관계 맺음.
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

# 1 : N 관계에서는 N쪽에서 1의 기본키를 가져야 한다. (to, on_delete 속성을 가져야 함)