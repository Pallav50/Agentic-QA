import os

import redis
from dotenv import load_dotenv

load_dotenv()


class CacheManager:
    def __init__(self):
        host = os.getenv("REDIS_HOST", "localhost")
        port = int(os.getenv("REDIS_PORT", 6379))
        try:
            self.client = redis.Redis(
                host=host,
                port=port,
                decode_responses=True,
                socket_connect_timeout=2,
            )
            self.client.ping()
            self.enabled = True
        except Exception:
            self.client = None
            self.enabled = False

    def get_healed_selector(self, broken_selector: str) -> str | None:
        if not self.enabled:
            return None
        try:
            return self.client.get(f"healed:{broken_selector}")
        except Exception:
            return None

    def save_healed_selector(self, broken_selector: str, new_selector: str):
        if not self.enabled:
            return
        try:
            self.client.set(f"healed:{broken_selector}", new_selector, ex=86400)
        except Exception:
            pass
