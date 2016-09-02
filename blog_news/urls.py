from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import *


urlpatterns = [
    url(r'^$', home_page_view),
    url(r'^blog/posts/(?P<post_id>[0-9])+$', single_blog_post_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)