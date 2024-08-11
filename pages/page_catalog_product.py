from playwright.sync_api import Page
from pages.components.navigation_bar import NavigationBar


class CatalogProductPage:

    def __init__(self, page: Page, navigation_bar: NavigationBar) -> None:
        self.page = page
        self.navigation_bar = navigation_bar
