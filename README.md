# Каталог товаров (Product & Category)

Учебный проект на Python: базовая ООП-модель интернет-магазина электроники.
Два класса — товар и категория товаров, категория ведёт учёт общего числа
созданных категорий и товаров во всех категориях.

## Описание

- `Product` — представляет товар и хранит его характеристики: название,
  описание, цену, количество на складе.
- `Category` — представляет категорию товаров, хранит список товаров и
  ведёт учёт через атрибуты класса:
  - `category_count` — сколько всего создано категорий;
  - `product_count` — сколько всего товаров во всех категориях (растёт
    при создании каждой новой категории на количество переданных в неё товаров).

## Структура проекта

```
main_14.1-main/
├── src/
│   ├── product.py       # класс Product
│   └── category.py      # класс Category
├── tests/
│   ├── test_product.py
│   └── test_category.py
└── main.py               # пример использования
```

## Установка и запуск

```bash
git clone git@github.com:Nesterov-art/main_14.1.git
cd main_14.1
poetry install
python main.py
```

## Тесты

```bash
pytest --cov
```

## Пример использования

```python
from src.product import Product
from src.category import Category

phone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
category = Category("Смартфоны", "Смартфоны и аксессуары", [phone])

print(Category.category_count)  # 1
print(Category.product_count)   # 1
```
