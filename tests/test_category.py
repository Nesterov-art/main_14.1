import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_add_valid_product():
    """Проверяет добавление корректного товара"""
    category = Category("Смартфоны", "Категория смартфонов")
    product = Product("iPhone", "Флагманский смартфон", 100000.0, 10)

    category.add_product(product)

    assert len(category.products) == 1
    assert "iPhone, 100000.0 руб. Остаток: 10 шт." in category.products


def test_add_invalid_product():
    """Проверяет, что нельзя добавить объект не типа Product"""
    category = Category("Телевизоры", "Категория телевизоров")

    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        category.add_product("не продукт")  # Передаем строку вместо объекта Product
