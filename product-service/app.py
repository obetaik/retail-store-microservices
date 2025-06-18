from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 350.25},
    {"id": 2, "name": "Smartphone", "price": 400.00},
    {"id": 3, "name": "Headphones", "price": 149.99}
]

@app.route('/product', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return jsonify(product) if product else ("Not found", 404)

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
