from celery import shared_task

from urls_app.models import Url
from aiohttp import ClientSession
import asyncio


async def make_request(url: str, session: ClientSession, responses: list) -> None:
    resp = await session.request(method="GET", url=url)
    resp.raise_for_status()

    resp_dict = {
        'url': url,
        'status': resp.status,
    }
    responses.append(resp_dict)


async def bulk_request(urls: list, responses: list) -> None:
    """Make requests concurrently"""
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                make_request(url, session, responses)
            )
        await asyncio.gather(*tasks)


@shared_task
def check_url_task():
    try:
        urls = Url.objects.filter(
            is_active=True,
            is_paused=False,
        )
        url_list = [url.text for url in urls]

        response_list = []
        asyncio.run(bulk_request(urls=url_list, responses=response_list))
        print(response_list)

        for resp in response_list:
            try:
                url = Url.objects.get(text=resp['url'])
                url.status = resp['status']
                url.save()
            except Url.DoesNotExist:
                pass

    except Exception as e:
        print(e)
