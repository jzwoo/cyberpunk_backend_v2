import httpx


GOOGLE_TOKEN_INFO_URL = "https://oauth2.googleapis.com/tokeninfo"


async def verify_access_token(access_token: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=GOOGLE_TOKEN_INFO_URL,
            params={"access_token": access_token},
        )

        response.raise_for_status()
        return response.json()
