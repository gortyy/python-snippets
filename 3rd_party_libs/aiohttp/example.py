import asyncio

import aiohttp


async def _get_json(session):
    try:
        response = await session.request(
            url="http://api.icndb.com/jokes/random", method="GET"
        )
    except Exception as exc:
        print(str(exc))
        return {}

    return await response.json()


async def get_json():
    async with aiohttp.ClientSession() as session:
        json = await _get_json(session)

    return json


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(
        asyncio.gather(*[get_json() for _ in range(100)])
    )

    for r in result:
        print(r.get("value", {}).get("joke", ""))
