import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

TARGET_URLS = [
    "https://ai.atomgit.com/zai-org/GLM-5/model-inference",
    "https://ai.atomgit.com/hf_mirrors/Qwen/Qwen3.5-397B-A17B/model-inference"
]
BUTTON_SELECTOR = "text=免费领取【无限token】"
LOGIN_URL = "https://ai.atomgit.com/login"


def load_credentials():
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    username = os.getenv("ATOMGIT_USERNAME")
    password = os.getenv("ATOMGIT_PASSWORD")
    if not username or not password:
        print("Error: ATOMGIT_USERNAME and ATOMGIT_PASSWORD must be set in .env file")
        sys.exit(1)
    return username, password


def login_and_click(page, username, password):
    print(f"Navigating to {LOGIN_URL}")
    page.goto(LOGIN_URL)
    page.wait_for_load_state("networkidle")

    print("Filling login form")
    page.fill('input[name="username"], input[type="text"]', username)
    page.fill('input[name="password"], input[type="password"]', password)
    page.click('button[type="submit"], button:has-text("登录")')
    page.wait_for_load_state("networkidle")
    print("Login completed")


def click_free_token_button(page, url):
    print(f"Navigating to {url}")
    page.goto(url)
    page.wait_for_load_state("networkidle")

    print(f"Looking for button: {BUTTON_SELECTOR}")
    try:
        button = page.locator(BUTTON_SELECTOR).first
        if button.is_visible():
            button.click()
            print(f"Clicked button on {url}")
            page.wait_for_timeout(2000)
        else:
            print(f"Button not visible on {url}")
    except Exception as e:
        print(f"Error clicking button on {url}: {e}")


def main():
    username, password = load_credentials()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        login_and_click(page, username, password)

        for url in TARGET_URLS:
            click_free_token_button(page, url)

        browser.close()

    print("All tasks completed")


if __name__ == "__main__":
    main()