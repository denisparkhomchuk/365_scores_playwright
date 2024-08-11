from playwright.sync_api import Page
from pages.components.navigation_bar import NavigationBar

URL = 'https://www.onliner.by/'


class MainPage:

    def __init__(self, page: Page, navigation_bar: NavigationBar) -> None:
        self.page = page
        self.navigation_bar = navigation_bar

    def load(self) -> None:
        self.page.goto(URL)
