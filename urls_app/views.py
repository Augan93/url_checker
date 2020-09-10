from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from datetime import datetime
from django.http import JsonResponse

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


@login_required
def set_interval(request):
    if request.method == 'POST':
        interval_val = request.POST['interval']
        interval, created = IntervalSchedule.objects.get_or_create(
            every=interval_val,
            period=IntervalSchedule.SECONDS,
        )

        name = 'URL_CHECKER'
        try:
            task = PeriodicTask.objects.get(name=name)
            task.interval = interval
            task.save()

        except PeriodicTask.DoesNotExist:
            PeriodicTask.objects.create(
                interval=interval,
                name=name,
                task='urls_app.tasks.check_url_task',
                start_time=datetime.now(),
                last_run_at=None,
            )

        return JsonResponse({
            'status': 'ok',
        })


@login_required
def pause(request):
    url_id = request.GET.get('id')
    try:
        url = models.Url.objects.get(pk=url_id)
        url.is_paused = not url.is_paused
        url.save()
        return JsonResponse(
            {
                'status': 'ok',
                'is_paused': url.is_paused,
            },
        )

    except models.Url.DoesNotExist:
        return JsonResponse(
            {
                'status': 'not_found',
            },
            status=404,
        )


@login_required
def get_url_status(request):
    urls = models.Url.objects.filter(
        is_active=True,
        is_paused=False,
    )
    url_list = []
    for url in urls:
        url_list.append(
            {
                'id': url.id,
                'status': url.status or '-',
            }
        )

    return JsonResponse(
        {
            'urls': url_list,
        }
    )
