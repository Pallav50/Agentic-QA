# Agentic-QA | Self-Healing Test Automation Framework

An intelligent test automation framework leveraging generative AI (Gemini API) and Playwright to dynamically repair broken web element locators and UI selectors at runtime.

## Core Features
* **AI Self-Healing Layer:** Intercepts selector timeout exceptions and queries Gemini 2.5 Flash to synthesize updated locators from the runtime DOM.
* **Smart Caching with Redis:** Remembers resolved selectors across test suites to minimize LLM latency and API calls.
* **Non-blocking Execution:** Prevents fragile UI selector changes from failing entire CI regression pipelines.
* **CI/CD Integration:** Ready-to-run GitHub Actions workflow with integrated Redis service.

## Tech Stack
* **Language:** Python
* **E2E Engine:** Playwright, Pytest
* **AI Model:** Google Gemini API (`gemini-2.5-flash`)
* **Storage/Cache:** Redis
* **CI/CD:** GitHub Actions

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<username>/Agentic-QA.git
   cd Agentic-QA
   ```

2. **Set up Virtual Environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Linux/macOS: source venv/bin/activate
   pip install -r requirements.txt
   playwright install
   ```

3. **Configure Environment:**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_api_key_here
   REDIS_HOST=localhost
   REDIS_PORT=6379
   ```

4. **Run Tests:**
   ```bash
   pytest tests/
   ```
