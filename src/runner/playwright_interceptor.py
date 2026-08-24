from playwright.sync_api import Page

from src.cache.redis_manager import CacheManager
from src.healer.gemini_client import GeminiHealer


class SmartPage:
    def __init__(self, page: Page):
        self.page = page
        self.healer = GeminiHealer()
        self.cache = CacheManager()

    def find_and_click(self, selector: str, timeout_ms: int = 3000):
        # 1. Check if we already have a cached fix
        cached_selector = self.cache.get_healed_selector(selector)
        target = cached_selector if cached_selector else selector

        try:
            self.page.locator(target).click(timeout=timeout_ms)
        except Exception:
            print(
                f"[Agentic-QA] Locator failed: '{target}'. "
                "Initiating self-healing..."
            )

            # Extract DOM snippet for context
            dom_snippet = self.page.content()

            # Call Gemini to heal locator
            healed_selector = self.healer.suggest_locator(selector, dom_snippet)
            print(f"[Agentic-QA] Gemini resolved new locator: '{healed_selector}'")

            # Retry with healed locator
            self.page.locator(healed_selector).click(timeout=timeout_ms)

            # Cache for future runs
            self.cache.save_healed_selector(selector, healed_selector)
