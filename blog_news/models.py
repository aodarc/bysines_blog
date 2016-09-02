from django.contrib.auth.models import User
from django.db import models
# from tinymce.models import HTMLField

#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class News(models.Model):
    blog_news_img = models.ImageField(blank=True, upload_to='blog/posts/%Y/%m/%d')
    title = models.CharField(max_length=150, blank=False, db_index=True, unique=True)
    author = models.ForeignKey(to=User, blank=False)
    content = RichTextUploadingField(blank=True)
    created = models.DateField(auto_now_add=True)

    categories = models.ManyToManyField(to=Category, blank=False)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        verbose_name = 'News in blog'
        verbose_name_plural = 'News in blog'

    def __str__(self):
        return self.title
