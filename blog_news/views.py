import calendar

from django.shortcuts import render, get_object_or_404
from django.template.loader_tags import register

from .models import News


# Create your views here.


@register.filter
def month_name(month_number):
    return calendar.month_name[month_number]

def home_page_view(request):
    content = {'news': News.objects.last()}
    return render(request, 'main_page.html', content)


def single_blog_post_view(request, post_id):
    news = get_object_or_404(News, pk=1)
    content = {
        'news': news,
        'author': news.author.first_name + ' ' + news.author.last_name,
        'tags': news.tags.all()
    }

    return render(request, 'blog-single-with-right-sidebar.html', content)