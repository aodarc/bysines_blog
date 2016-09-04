from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language

# from tinymce.models import HTMLField

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return self.name


class Category(models.Model):
    name_uk = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)
    name_pl = models.CharField(max_length=25)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name_uk


class News(models.Model):
    author = models.ForeignKey(to=User, blank=False)

    blog_news_img = models.ImageField(blank=True, upload_to='blog/posts/%Y/%m/%d')

    title_uk = models.CharField(max_length=150, blank=False, db_index=True, unique=True)
    title_eng = models.CharField(max_length=150, blank=False, db_index=True, unique=True)
    title_pl = models.CharField(max_length=150, blank=False, db_index=True, unique=True)

    content_uk = RichTextUploadingField(blank=True)
    content_en = RichTextUploadingField(blank=True)
    content_pl = RichTextUploadingField(blank=True)

    created = models.DateField(auto_now_add=True)

    categories = models.ManyToManyField(to=Category, blank=False)
    tags = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        verbose_name = _('News in blog')
        verbose_name_plural = _('News in blog')

    # def get_short_post(self):
    #     post = self._get_translated_post()
    #     post['title'] = post.get('title')[:56]
    #     post['content'] = post.get('content')[:359] + '....'
    #
    #     return post

    def get_translated_post(self):
        # TODO overload GET method in django manager
        lg = get_language()

        if lg == 'uk':
            self.title = self.title_uk
            self.content = self.content_uk
        elif lg == 'en':
            self.title = self.title_en
            self.content = self.content_en
        else:
            self.title = self.title_pl
            self.content = self.content_pl

        # attributes = {
        #     'title': title,
        #     'content': content,
        #     'author': self.author,
        #     'pk': self.pk,
        #     'created': self.created,
        #     'categories': self.categories,
        #     'tags': self.tags
        # }
        return self

    def __str__(self):
        return self.title_uk


class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=30, blank=False)
    content = models.TextField(max_length=1000, blank=False)
    created = models.DateTimeField(auto_now_add=True, blank=False)

    post = models.ForeignKey(to=News, on_delete=models.CASCADE, related_name='comment')

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
        ordering = ('-created',)

    def __str__(self):
        return self.email + ' ' + self.name
