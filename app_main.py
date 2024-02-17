from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Fungsi untuk mendapatkan informasi produk dari app_product.py
def get_product_info(product_id):
    response = requests.get(f'http://localhost:5000/products/{product_id}')
    return response.json()

# Fungsi untuk mendapatkan jumlah kuantitas yang terjual dari app_cart.py
def get_sold_quantity(product_id):
    response = requests.get(f'http://localhost:5001/cart/quantity/{product_id}')
    return response.json()['total_quantity']

# Fungsi untuk mendapatkan ulasan produk dari app_comment.py
def get_product_reviews(product_id):
    response = requests.get(f'http://localhost:5003/reviews/{product_id}')
    return response.json()

@app.route('/product/<int:product_id>')
def show_product(product_id):
    # Mendapatkan informasi produk
    product_info = get_product_info(product_id)

    # Mendapatkan jumlah kuantitas yang terjual
    sold_quantity = get_sold_quantity(product_id)

    # Mendapatkan ulasan produk
    product_reviews = get_product_reviews(product_id)

    return render_template('newindex.html', product=product_info, sold_quantity=sold_quantity, reviews=product_reviews)

if __name__ == '__main__':
    app.run(debug=True, port=5004)
