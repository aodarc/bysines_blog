import calendar

from django.shortcuts import render, get_object_or_404
from django.template.loader_tags import register
from django.utils.translation import get_language

from .models import News


# Create your views here.


@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]


def home_page_view(request):
    content = {'news': News.objects.all()[:6]}

    print(News.objects.last().get_translated_post().title)
    # 56 title
    # 359 + 4.
    return render(request, 'main_page.html', content)


def single_blog_post_view(request, post_id):
    print(get_language())
    news = get_object_or_404(News, pk=1)
    content = {
        'news': news,
        'author': news.author.first_name + ' ' + news.author.last_name,
        'tags': news.tags.all()
    }

    return render(request, 'blog-single-with-right-sidebar.html', content)


def add_comment_view(request):
    return render(request, )