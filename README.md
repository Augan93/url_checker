"# url_checker" 
Go to http://127.0.0.1:8000/urls/
Admin: http://127.0.0.1:8000/admin/

URLs are checked periodically with given interval via Celery.
All requests are made concurrently using asyncio and aiohttp packages.

UI sends request periodically to the server for fetching URLs.
Individual URL can be paused and resumed. If an url was paused then the url are not checked by Celery task.


Start Celery worker:
celery -A url_checker worker --loglevel=info

Start Celert beat:
celery -A url_checker beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
