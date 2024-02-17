from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for product reviews
product_reviews  = [
    {"user_id": 1, "product_id": 1, "review": "Very Kereeen"},
    {"user_id": 1, "product_id": 3, "review": "Good Quality"},
    {"user_id": 2, "product_id": 2, "review": "Not great"},
    {"user_id": 2, "product_id": 1, "review": "The Bessst"}
]

@app.route('/reviews')
def get_cart():
    return jsonify(product_reviews)

# Route to get reviews of a product
@app.route('/reviews/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = [review for review in product_reviews if review['product_id'] == product_id]
    if reviews:
        return jsonify({'product_id': product_id, 'reviews': reviews})
    else:
        return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5003)
