from django.db import models

class Detection(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='intruder_images/')
    created_at = models.DateTimeField(auto_now_add=True)  # 记录创建时间
    published_at = models.DateTimeField(auto_now=True)  # 记录最后一次更新的时间

    def __str__(self):
        return self.title
