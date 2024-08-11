import pytest
import allure

from pages.page_main import MainPage
from pages.page_catalog import CatalogPage
from pages.page_catalog_product import CatalogProductPage
from playwright.sync_api import expect, Page


@allure.title("Onliner Catalog navigation test")
@pytest.mark.parametrize('section,subsection,subsubsection,expected_page_title', [
    ('Электроника', 'Телевидение и видео', 'Телевизоры1', 'Телевизор купить'),
    ('Бытовая техника', 'Уборка', 'Роботы-пылесосы', 'Робот-пылесос купить')
])
def test_catalog(
        section,
        subsection,
        subsubsection,
        expected_page_title,
        page: Page,
        page_main: MainPage,
        page_catalog: CatalogPage,
        page_catalog_product: CatalogProductPage,
        screenshot_after) -> None:
    page_main.load()
    page_main.navigation_bar.goto_catalog()
    page_catalog.goto_section(section)
    page_catalog.goto_subsection(subsection)
    page_catalog.goto_subsubsection(subsubsection)
    expect(page_catalog_product.page).to_have_title(expected_page_title)
