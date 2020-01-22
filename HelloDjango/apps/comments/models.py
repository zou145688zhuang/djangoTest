from django.db import models
from django.utils import timezone
# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=50,verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    url = models.URLField(verbose_name='网址',blank=True)
    text = models.TextField(verbose_name='评论内容')
    create_time = models.DateTimeField(verbose_name='评论时间',default=timezone.now())
    post = models.ForeignKey('blog.Post',verbose_name='文章',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']

    def __str__(self):
        return '{}:{}'.format(self.name,self.text[:10])