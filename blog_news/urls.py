from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import *


urlpatterns = [
    url(r'^$', home_page_view, name='home'),
    url(r'^blog/posts/(?P<post_id>[0-9]+)$', single_blog_post_view, name='blog_post'),
    url(r'^blog/post/(?P<post_id>[0-9]+)/add_comment$', add_comment_view, name='add_comment'),
    url(r'^blog/archive/', NewsListView.as_view(), name='blog_archive'),
    url(r'^contact$', contact_view, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)