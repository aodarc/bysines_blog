"""htdocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView

from .views import set_language

urlpatterns = [
    # url(r'^i18n/', include('django.conf.urls.i18n'), name='set_language'),
    url(r'^set_language/$', set_language, name='set_language'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog_news.urls')),
    url(r'^service$', TemplateView.as_view(template_name='service.html'), name='service')
)

handler404 = 'blog_news.views.page404'
