from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for products
products = [
    {"id": 1, "name": "Product 1", "description": "Description for Product 1", "price": 10},
    {"id": 2, "name": "Product 2", "description": "Description for Product 2", "price": 20},
    {"id": 3, "name": "Product 3", "description": "Description for Product 3", "price": 30}
]

# all products
@app.route('/products')
def get_products():
    return jsonify(products)

# get single product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return jsonify(product)
    return jsonify({"error": "Product not found"}), 400
        
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
