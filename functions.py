from playwright.sync_api import sync_playwright
import time
import streamlit as st

start = time.time()

def cb_find(url, search_query):
    with sync_playwright() as p:
        # Configure for GitHub Actions (headless + browser setup)
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            # Navigate to login page
            page.goto(url, timeout=60000)


            page_content = page.content().lower()

            if search_query.lower() in page_content:
                return True
            else:
                return False

        except Exception as e:
            st.text(f"Error: {str(e)}")
        finally:
            browser.close()


cb_find("https://en.wikipedia.org/wiki/Apple", "apple")
print(f"took {time.time() - start} seconds.")