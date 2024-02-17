from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for cart
cart_items = [
    {"user_id": 1, "product_id": 1, "quantity": 2},
    {"user_id": 1, "product_id": 2, "quantity": 1},
    {"user_id": 2, "product_id": 1, "quantity": 1}
]

@app.route('/cart')
def get_cart():
    return jsonify(cart_items)

# Route to get total quantity of a product in the cart
@app.route('/cart/quantity/<int:product_id>', methods=['GET'])
def get_total_quantity(product_id):
    total_quantity = sum(item['quantity'] for item in cart_items if item['product_id'] == product_id)
    return jsonify({'product_id': product_id, 'total_quantity': total_quantity})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
