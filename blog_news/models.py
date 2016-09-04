from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=25, blank=False, db_index=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=25, blank=False, db_index=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name_uk


class News(models.Model):
    author = models.ForeignKey(to=User, blank=False)

    blog_news_img = models.ImageField(blank=True, upload_to='blog/posts/%Y/%m/%d')

    title = models.CharField(max_length=150, blank=True, db_index=True, unique=True)
    content = RichTextUploadingField(blank=True)

    created = models.DateField(auto_now_add=True)

    categories = models.ManyToManyField(to=Category, blank=False)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        verbose_name = _('News in blog')
        verbose_name_plural = _('News in blog')

    def __str__(self):
        return self.title_uk


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False)

    # TODO overide on_delete method
    post = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-created',)

    def __str__(self):
        return self.email + ' ' + self.name
