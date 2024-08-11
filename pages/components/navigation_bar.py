from playwright.sync_api import Page
import allure


class NavigationBar:
    SECTION_NAME_CATALOG = 'Каталог'

    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, section_name):
        with allure.step(f'Navigate to section "{section_name}"'):
            self._get_navigation_bar_section_locator(section_name).click()

    def goto_catalog(self):
        self.goto(self.SECTION_NAME_CATALOG)

    def _get_navigation_bar_section_locator(self, section_name):
        return self.page.locator(LocatorSelectors.NAVIGATION_BAR_CONTAINER).get_by_text(section_name)


class LocatorSelectors:
    NAVIGATION_BAR_CONTAINER = 'nav[class="b-top-navigation"]'
