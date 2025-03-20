from src.product import Product

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

    def add_product(self, product: Product):
        """Добавляет товар в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Выводит список товаров в формате: Название, цена руб. Остаток: N шт."""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
