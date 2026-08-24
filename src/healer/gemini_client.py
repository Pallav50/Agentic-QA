import os

from dotenv import load_dotenv
from google import genai

load_dotenv()


class GeminiHealer:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key) if api_key else None

    def suggest_locator(self, broken_selector: str, page_dom: str) -> str:
        if not self.client:
            raise ValueError("GEMINI_API_KEY is not configured.")

        prompt = f"""
        You are an expert QA automation engineer. A UI test locator has broken.

        Original Broken Selector: {broken_selector}
        Current Page DOM Snippet:
        {page_dom[:3000]}

        Identify the intended target element and return ONLY the most robust, updated CSS selector or XPath.
        Return raw selector string only without backticks or explanations.
        """
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text.strip()
