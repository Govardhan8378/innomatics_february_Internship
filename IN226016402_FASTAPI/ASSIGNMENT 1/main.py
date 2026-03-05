from fastapi import FastAPI, Query

app = FastAPI()

# Temporary data 

products = [

    {'id': 1, 'name': 'Wireless Mouse', 'price': 499,  'category': 'Electronics', 'in_stock': True },

    {'id': 2, 'name': 'Notebook', 'price':  50,  'category': 'Stationery',  'in_stock': True },

    {'id': 3, 'name': 'USB Hub','price': 599, 'category': 'Electronics', 'in_stock': False},

    {'id': 4, 'name': 'Pen Set','price':  99, 'category': 'Stationery',  'in_stock': True },

# Task 1 — Add More Products 

    {"id": 5, "name": "Laptop Stand", "price": 1499, "category": "Electronics", "in_stock": True},

    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},

    {"id": 7, "name": "Webcam", "price": 1999, "category": "Electronics", "in_stock": False}

]


#  Endpoint 0 — Home 

@app.get('/')

def home():

    return {'message': 'Welcome to our E-commerce API'}

 

# ── Endpoint 1 — Return all products ──────────────────────────

@app.get('/products')

def get_all_products():

    return {'products': products, 'total': len(products)}

@app.get('/products/filter')

def filter_products(

    category:  str  = Query(None, description='Electronics or Stationery'),

    max_price: int  = Query(None, description='Maximum price'),

    in_stock:  bool = Query(None, description='True = in stock only')

):

    result = products          # start with all products

    if category:

        result = [p for p in result if p['category'] == category]

    if max_price:

        result = [p for p in result if p['price'] <= max_price]


    if in_stock is not None:

        result = [p for p in result if p['in_stock'] == in_stock]

    return {'filtered_products': result, 'count': len(result)}



# ── Task 2  Filter Products by Category 
@app.get('/products/category/{category_name}')
def get_products_by_category(category_name: str):
    
    result = [p for p in products 
              if p['category'].lower() == category_name.lower()]
    
    return {
        "category": category_name,
        "products": result,
        "count": len(result)
    }

# ── Task 3  Return products that are in stock

@app.get('/products/instock')
def get_instock_products():
    instock = [product for product in products if product['in_stock']]
    return {
        "in_stock_products": instock,
        "count": len(instock)
    }


# Task 4  Store Summary
@app.get('/store/summary')
def store_summary():

    store_name = "My E-commerce Store"

    total_products = len(products)

    instock = sum(product['in_stock'] for product in products)

    out_of_stock = total_products - instock

    categories = list({product['category'] for product in products})

    return {
        "store_name": store_name,
        "total_products": total_products,
        "in_stock": instock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }


# Task 5 — Search Products by Name

@app.get('/products/search/{keyword}')
def search_products(keyword: str):

    result = [
        product for product in products
        if keyword.lower() in product['name'].lower()
    ]

    if not result:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": result,
        "count": len(result)
    }


# Bonus Task — Cheapest & Most Expensive Product ─────────────

@app.get("/products/deals")
def get_deals():

    cheapest = min(products, key=lambda p: p["price"])

    expensive = max(products, key=lambda p: p["price"])

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }


# ── Endpoint 3 — Return one product by its ID  ─────────────────

@app.get('/products/{product_id}')
def get_product(product_id: int):

    for product in products:
        if product['id'] == product_id:
            return {"product": product}

    return {"error": "Product not found"}