from django.db import models
from  cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Image(models.Model):
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        image = CloudinaryField('image')
        website = models.CharField(max_length=100)
        comments = models.IntegerField(default=0)
        description = models.TextField(null=True, blank=True)
        created = models.DateTimeField(auto_now_add=True)
        class Meta:
            ordering = ['-created']
        # def __str__(self):
        #     return self.username

class Comment(models.Model):
    design = models.IntegerField(null=True, default=0)
    usability = models.IntegerField(null=True, default=0)
    content = models.IntegerField(null=True, default=0)
    total = models.FloatField(max_length=8, blank=True, null=True, default= 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Image, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
      ordering = ['-created']

    def __str__(self):
        return self.body[0:50]
