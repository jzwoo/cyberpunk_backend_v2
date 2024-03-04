import motor.motor_asyncio
import os

MONGO_DB_URI = os.environ.get("MONGO_DB_URI")
MONGO_USERNAME = os.environ.get("MONGO_USERNAME")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")

MONGO_DATABASE = "cyberpunk-db"


def get_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        MONGO_DB_URI, username=MONGO_USERNAME, password=MONGO_PASSWORD
    )

    return client[MONGO_DATABASE]
