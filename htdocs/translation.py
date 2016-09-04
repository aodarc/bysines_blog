from modeltranslation.translator import translator, TranslationOptions
from blog_news.models import News, Category


class NewsTranslationOptions(TranslationOptions):

    fields = ('title', 'content',)

class CategoryTranslationOptions(TranslationOptions):

    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)
translator.register(News, NewsTranslationOptions)