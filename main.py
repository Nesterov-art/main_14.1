from src.product import Product
from src.category import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")

    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)


    print(category1.name)
    print(category1.description)
    print(category1.products)
    print(Category.category_count)
    print(Category.product_count)


    product_data = {"name": "55\" QLED 4K", "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
    product4 = Product.new_product(product_data)


    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником")

    category2.add_product(product4)

    print(category2.name)
    print(category2.description)
    print(category2.products)
    print(Category.category_count)
    print(Category.product_count)


    product4.price = -5000
    print(product4.price)
