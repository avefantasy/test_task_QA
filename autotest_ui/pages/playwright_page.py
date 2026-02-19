from playwright.sync_api import Page, expect

class PlaywrightPage:

    URL = "https://playwright.dev/"
    TITLE_TEXT = "Fast and reliable end-to-end testing for modern web apps | Playwright"

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)

    def check_page_title(self):
        expect(self.page).to_have_title(self.TITLE_TEXT)

