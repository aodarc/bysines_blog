from django.contrib import admin
from django.db import models
from modeltranslation.translator import TranslationOptions, translator

from .models import News, Tag, Category, Contact

# Register your models here.
from ckeditor.widgets import CKEditorWidget
from modeltranslation.admin import TabbedTranslationAdmin


class NewsTranslationOptions(TranslationOptions):

    fields = ('title', 'content', 'description')


class CategoryTranslationOptions(TranslationOptions):

    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)
translator.register(News, NewsTranslationOptions)


class CategoryAdmin(TabbedTranslationAdmin):
    pass


class NewsAdmin(TabbedTranslationAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
admin.site.register(Contact)
