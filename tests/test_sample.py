from playwright.sync_api import Page

from src.runner.playwright_interceptor import SmartPage


def test_smart_navigation(page: Page):
    smart = SmartPage(page)
    page.goto("https://playwright.dev/")
    # Demonstrates clicking with resilience
    smart.find_and_click("a.getStarted_Sjon")
