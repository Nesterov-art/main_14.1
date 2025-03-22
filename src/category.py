from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.__products = []  # Приватный список товаров

        Category.category_count += 1

    def add_product(self, product):
        """Добавляет товар в категорию, если это объект класса Product или его наследник"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает список товаров в отформатированном виде"""
        return [f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products]
