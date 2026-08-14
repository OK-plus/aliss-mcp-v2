import httpx


ALISS_API = "https://api.aliss.org/v4/services/"


async def search_aliss(postcode: str, keyword: str, radius: int = 10):
    params = {
        "postcode": postcode,
        "q": keyword,
        "distance": radius,
    }

    async with httpx.AsyncClient(
        timeout=20,
        follow_redirects=True,
    ) as client:
        response = await client.get(ALISS_API, params=params)

    response.raise_for_status()

    data = response.json()

    results = []

    for service in data.get("results", [])[:10]:
        results.append(
            {
                "name": service.get("name"),
                "description": service.get("description"),
                "address": service.get("address"),
                "phone": service.get("phone"),
                "email": service.get("email"),
                "website": service.get("website"),
            }
        )

    return results
