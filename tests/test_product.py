from src.product import Product


def test_product_initialization():
    """Проверяет правильность создания товара"""
    product = Product("Test Product", "Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_new_product():
    """Проверяет создание товара через класс-метод"""
    data = {"name": "Laptop", "description": "Gaming laptop", "price": 150000.0, "quantity": 3}
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Laptop"
    assert product.description == "Gaming laptop"
    assert product.price == 150000.0
    assert product.quantity == 3


def test_product_price_setter():
    """Проверяет работу сеттера цены"""
    product = Product("Phone", "Smartphone", 50000.0, 5)

    product.price = 45000.0
    assert product.price == 45000.0

    product.price = -1000.0
    assert product.price == 45000.0

    product.price = 0
    assert product.price == 45000.0

def test_product_str():
    product = Product("Тестовый товар", "Описание", 100.0, 10)
    assert str(product) == "Тестовый товар, 100 руб. Остаток: 10 шт."

def test_product_add():
    a = Product("A", "desc", 100, 10)  # 1000
    b = Product("B", "desc", 200, 2)   # 400
    assert a + b == 1400

def test_product_add_typeerror():
    a = Product("A", "desc", 100, 10)
    try:
        _ = a + 5  # не Product
        assert False, "TypeError должен быть вызван"
    except TypeError:
        assert True