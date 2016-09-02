from django.contrib import admin

from .models import News, Tag, Category

# Register your models here.
from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(News, PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
