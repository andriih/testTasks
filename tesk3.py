def sort_products(products, sort_key, ascending=True):
    return sorted(products, key=lambda x: x[sort_key], reverse=not ascending)

products = [
    {"name": "Product A", "price": 100, "stock": 5},
    {"name": "Product B", "price": 200, "stock": 3},
    {"name": "Product C", "price": 50, "stock": 10}
]
sort_key = "name"
ascending = True

sorted_products = sort_products(products, sort_key, ascending)

print(sorted_products)
