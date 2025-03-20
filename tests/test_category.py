import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_category_and_product_count():
    """Проверяет счетчики категорий и товаров"""
    category1 = Category("Category1", "Description1")
    category2 = Category("Category2", "Description2")

    product1 = Product("Product1", "Desc1", 50.0, 5)
    product2 = Product("Product2", "Desc2", 75.0, 3)

    category1.add_product(product1)
    category2.add_product(product2)

    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_initialization():
    """Проверяет создание категории и добавление товаров"""
    category = Category("Test Category", "Category Description")

    product1 = Product("Product1", "Desc1", 50.0, 5)
    product2 = Product("Product2", "Desc2", 75.0, 3)

    category.add_product(product1)
    category.add_product(product2)

    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert len(category.products) == 2
    assert "Product1, 50.0 руб. Остаток: 5 шт." in category.products
    assert "Product2, 75.0 руб. Остаток: 3 шт." in category.products
