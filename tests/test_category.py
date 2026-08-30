import pytest
from src.product import Product
from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counts():
    """Сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


def test_init_without_products():
    """Создание категории без продуктов"""
    category = Category("Ноутбуки", "Категория ноутбуков")

    assert category.name == "Ноутбуки"
    assert category.description == "Категория ноутбуков"
    assert category.products == []
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_init_with_products():
    """Создание категории с продуктами"""
    p1 = Product("MacBook", "Apple ноутбук", 200000, 5)
    p2 = Product("Asus", "Игровой ноутбук", 150000, 3)
    category = Category("Ноутбуки", "Категория ноутбуков", [p1, p2])

    assert len(category.products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2
    assert category.products == [
        "MacBook, 200000 руб. Остаток: 5 шт.",
        "Asus, 150000 руб. Остаток: 3 шт."
    ]


def test_add_valid_product():
    """Проверка добавления корректного товара"""
    category = Category("Смартфоны", "Категория смартфонов")
    product = Product("iPhone", "Флагманский смартфон", 100000.0, 10)

    category.add_product(product)

    assert len(category.products) == 1
    assert "iPhone, 100000.0 руб. Остаток: 10 шт." in category.products
    assert Category.product_count == 1


def test_add_invalid_product_raises_typeerror():
    """Нельзя добавить объект не Product"""
    category = Category("Телевизоры", "Категория телевизоров")

    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        category.add_product("не продукт")  # строка, не Product


def test_category_str_with_products():
    """Проверка __str__ у категории с продуктами"""
    p1 = Product("A", "desc", 100, 10)
    p2 = Product("B", "desc", 200, 5)
    cat = Category("Электроника", "Описание", [p1, p2])

    assert str(cat) == "Электроника, количество продуктов: 15 шт."


def test_category_str_without_products():
    """Проверка __str__ у категории без продуктов"""
    cat = Category("Аксессуары", "Описание")

    assert str(cat) == "Аксессуары, количество продуктов: 0 шт."


def test_products_property_format():
    """Корректность форматирования вывода продуктов"""
    p1 = Product("Test1", "desc", 150, 1)
    p2 = Product("Test2", "desc", 200, 3)
    cat = Category("Смартфоны", "desc", [p1, p2])

    assert cat.products == [
        "Test1, 150 руб. Остаток: 1 шт.",
        "Test2, 200 руб. Остаток: 3 шт."
    ]
