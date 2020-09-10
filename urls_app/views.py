from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import models


@login_required
def urls(request):
    urls = models.Url.objects.filter(is_active=True)
    context = {
        'urls': urls,
    }

    return render(
        request,
        'urls_app/url_list.html',
        context=context,
    )
