from typing import List, Dict

def get_affordable_products(products: List[Dict[str, any]], max_price: float) -> List[str]:
    affordable_products = []
    for product in products:
        if product['price'] <= max_price:
            affordable_products.append(product['product'])
    return affordable_products

def test_no_affordable_products():
    products = [
        {'product': 'bread', 'price': 10},
        {'product': 'milk', 'price': 15},
        {'product': 'cheese', 'price': 20}
    ]
    max_price = 5
    assert get_affordable_products(products, max_price) == []

def test_all_affordable_products():
    products = [
        {'product': 'bread', 'price': 10},
        {'product': 'milk', 'price': 15},
        {'product': 'cheese', 'price': 20}
    ]
    max_price = 50
    assert get_affordable_products(products, max_price) == ['bread', 'milk', 'cheese']

def test_partial_affordable_products():
    products = [
        {'product': 'bread', 'price': 10},
        {'product': 'milk', 'price': 15},
        {'product': 'cheese', 'price': 20}
    ]
    max_price = 12
    assert get_affordable_products(products, max_price) == ['bread']

def test_empty_product_list():
    products = []
    max_price = 50
    assert get_affordable_products(products, max_price) == []



