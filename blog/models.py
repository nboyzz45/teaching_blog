from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=20)
    slug = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True, null=False)
    content = RichTextField()
    pub_date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
