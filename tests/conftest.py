import pytest
import allure

from pages.page_main import MainPage
from pages.page_catalog import CatalogPage
from pages.page_catalog_product import CatalogProductPage
from pages.components.navigation_bar import NavigationBar
from playwright.sync_api import Page


@pytest.fixture
def page_main(page: Page) -> MainPage:
    navigation_bar = NavigationBar(page)
    return MainPage(page, navigation_bar)


@pytest.fixture
def page_catalog(page: Page) -> CatalogPage:
    navigation_bar = NavigationBar(page)
    return CatalogPage(page, navigation_bar)


@pytest.fixture
def page_catalog_product(page: Page) -> CatalogProductPage:
    navigation_bar = NavigationBar(page)
    return CatalogProductPage(page, navigation_bar)


@pytest.fixture
def screenshot_after(page: Page):
    yield
    allure.attach(page.screenshot(type='png'), name=f'test_end_screenshot.png', attachment_type=allure.attachment_type.PNG)
