from autotest_ui.pages.playwright_page import PlaywrightPage

def test_playwright_title(browser_page):
    playwright_page = PlaywrightPage(browser_page)

    playwright_page.open()
    playwright_page.check_page_title()





