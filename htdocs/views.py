from django import http
from django.conf import settings
from django.core.urlresolvers import translate_url
from django.utils.http import is_safe_url
from django.utils.translation import (
    LANGUAGE_SESSION_KEY, check_for_language,
)

LANGUAGE_QUERY_PARAMETER = 'language'


def set_language(request):
    """
    Redirect to a given url while setting the chosen language in the
    session or cookie. The url and the language code need to be
    specified in the request parameters.

    Since this view changes how the user will see the rest of the site, it must
    only be accessed as a POST request. If called as a GET request, it will
    redirect to the page in the request (the 'next' parameter) without changing
    any state.
    """
    next = request.POST.get('next', request.GET.get('next'))
    if not is_safe_url(url=next, host=request.get_host()):
        next = request.META.get('HTTP_REFERER')
        if not is_safe_url(url=next, host=request.get_host()):
            next = '/'
    response = http.HttpResponseRedirect(next)
    if request.method == 'GET':
        lang_code = request.GET.get(LANGUAGE_QUERY_PARAMETER)
        if lang_code and check_for_language(lang_code):
            next_trans = translate_url(next, lang_code)
            if next_trans != next:
                response = http.HttpResponseRedirect(next_trans)
            if hasattr(request, 'session'):
                request.session[LANGUAGE_SESSION_KEY] = lang_code
            else:
                response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code,
                                    max_age=settings.LANGUAGE_COOKIE_AGE,
                                    path=settings.LANGUAGE_COOKIE_PATH,
                                    domain=settings.LANGUAGE_COOKIE_DOMAIN)
    return response
