from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('タイトル', max_length=30)
    text = models.TextField('本文')
    is_public = models.BooleanField('公開可能か', default=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)
    updated_at = models.DateTimeField('更新日', default=timezone.now)

    def __str__(self):
        return self.title

# Create your models here.
