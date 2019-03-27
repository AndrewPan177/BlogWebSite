from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class BlogArticles(models.Model):
    title=models.CharField(max_length=30)
    author=models.ForeignKey(User,related_name="blog_posts",on_delete=models.CASCADE)
    body=models.TextField()
    publish=models.DateField(default=timezone.now)

    class Meta:
        ordering=("id",)

    def __str__(self):
        return self.title

