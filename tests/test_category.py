import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts():
    Category.category_count = 0
    Category.product_count = 0


def test_category_and_product_count():
    product1 = Product("Product1", "Desc1", 50.0, 5)
    product2 = Product("Product2", "Desc2", 75.0, 3)

    category1 = Category("Category1", "Description1", [product1])
    category2 = Category("Category2", "Description2", [product2])

    assert Category.category_count == 2
    assert Category.product_count == 2


def test_category_initialization():
    product1 = Product("Product1", "Desc1", 50.0, 5)
    product2 = Product("Product2", "Desc2", 75.0, 3)

    category = Category("Test Category", "Category Description", [product1, product2])

    assert category.name == "Test Category"
    assert category.description == "Category Description"
    assert len(category.products) == 2
    assert category.products[0] is product1
    assert category.products[1] is product2