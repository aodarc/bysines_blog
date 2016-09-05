from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

to_translate ={
    'Categories': _('Categories'),

}


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

    title = models.CharField(max_length=150, blank=False, db_index=True, unique=True, verbose_name=_('Title'))
    content = RichTextUploadingField(blank=False, verbose_name=_('Content'))
    description = models.CharField(max_length=255, blank=False, verbose_name=_('Description'))

    created = models.DateField(auto_now_add=True, verbose_name=_('Created'))

    categories = models.ManyToManyField(to=Category, blank=False, verbose_name=_('Categories'))
    tags = models.ManyToManyField(to=Tag, blank=True, verbose_name=_('Tags'))

    class Meta:
        verbose_name = _('News in blog')
        verbose_name_plural = _('News in blog')

    def __str__(self):
        return self.title_uk


class Comment(models.Model):
    email = models.EmailField(verbose_name=_('Email'))
    name = models.CharField(max_length=30, blank=False, verbose_name=_('Name'))
    content = models.TextField(max_length=1000, blank=False, verbose_name=_('Content'))
    created = models.DateTimeField(auto_now_add=True, blank=False, verbose_name=_('Created'))

    # TODO overide on_delete method
    post = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-created',)

    def __str__(self):
        return self.email + ' ' + self.name
