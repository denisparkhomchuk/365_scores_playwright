from playwright.sync_api import Page
from pages.components.navigation_bar import NavigationBar
import allure


class CatalogPage:

    def __init__(self, page: Page, navigation_bar: NavigationBar) -> None:
        self.page = page
        self.navigation_bar = navigation_bar

    def goto_section(self, section_name):
        self.page.wait_for_load_state()
        with allure.step(f'Navigate to section "{section_name}"'):
            self._get_catalog_section_locator(section_name).click()

    def goto_subsection(self, subsection_name):
        with allure.step(f'Navigate to subsection "{subsection_name}"'):
            self._get_catalog_subsection_locator(subsection_name).click()

    def goto_subsubsection(self, subsubsection_name):
        with allure.step(f'Navigate to subsubsection "{subsubsection_name}"'):
            self._get_catalog_subsubsection_locator(subsubsection_name).click()

    def _get_catalog_section_locator(self, section_name):
        return self._get_catalog_section_hierarchy_locator(LocatorSelectors.CATALOG_SECTIONS_CONTAINER,
                                                           LocatorSelectors.CATALOG_SECTION_NAME_CONTAINER,
                                                           section_name)

    def _get_catalog_subsection_locator(self, subsection_name):
        return self._get_catalog_section_hierarchy_locator(LocatorSelectors.CATALOG_SUBSECTIONS_CONTAINER,
                                                           LocatorSelectors.CATALOG_SUBSECTION_NAME_CONTAINER,
                                                           subsection_name)

    def _get_catalog_subsubsection_locator(self, subsubsection_name):
        return self._get_catalog_section_hierarchy_locator(LocatorSelectors.CATALOG_SUBSUBSECTIONS_CONTAINER,
                                                           LocatorSelectors.CATALOG_SUBSUBSECTION_NAME_CONTAINER,
                                                           subsubsection_name)

    def _get_catalog_section_hierarchy_locator(self, container, name_container, name):
        return self.page.locator(container).locator(name_container).get_by_text(name)


class LocatorSelectors:
    CATALOG_SECTIONS_CONTAINER = 'ul[class="catalog-navigation-classifier"]'
    CATALOG_SUBSECTIONS_CONTAINER = 'div[class="catalog-navigation-list__aside-list"]'
    CATALOG_SUBSUBSECTIONS_CONTAINER = 'div[class="catalog-navigation-list__dropdown-list"]'
    CATALOG_SECTION_NAME_CONTAINER = 'span[class="catalog-navigation-classifier__item-title-wrapper"]'
    CATALOG_SUBSECTION_NAME_CONTAINER = 'div[class="catalog-navigation-list__aside-title"]'
    CATALOG_SUBSUBSECTION_NAME_CONTAINER = 'span[class="catalog-navigation-list__dropdown-title"]'
