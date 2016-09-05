from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from blog_news.forms import CommentForm
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
    print(request.path_info)
    return render(request, 'main_page.html', content)


def single_blog_post_view(request, post_id):
    news = get_object_or_404(News, pk=post_id)

    content = {
        'news': news,
    }

    return render(request, 'blog-single-with-right-sidebar.html', content)


def add_comment_view(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(News, pk=post_id)
            comment.save()

        return redirect('blog_post', post_id=post_id)
    else:
        raise Http404("Method not allowed")