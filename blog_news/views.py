import calendar

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import News


# Create your views here.


class NewsListView(ListView):

    model = News
    template_name = 'blog-archive.html'
    paginate_by = 3


def home_page_view(request):
    content = {'news': News.objects.all()[:6]}

    # 56 title
    # 359 + 4.
    return render(request, 'main_page.html', content)


def single_blog_post_view(request, post_id):
    news = get_object_or_404(News, pk=post_id)

    content = {
        'news': news,
    }

    return render(request, 'blog-single-with-right-sidebar.html', content)


def add_comment_view(request):
    return render(request, )