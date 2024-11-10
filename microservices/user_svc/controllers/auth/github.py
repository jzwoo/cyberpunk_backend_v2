import httpx


async def get_user_details(access_token: str):
    async with httpx.AsyncClient(
        headers={"Authorization": f"Bearer {access_token}"}
    ) as client:
        response = await client.get(url="https://api.github.com/user")

        response.raise_for_status()

        return response.json()
