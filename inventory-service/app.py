# Inventory Service (inventory-service/app.py)
from flask import Flask, jsonify

app = Flask(__name__)

stock = {
    "1": 50,
    "2": 200
}

@app.route('/inventory/<product_id>')
def get_stock(product_id):
    quantity = stock.get(product_id, 0)
    return jsonify({"product_id": product_id, "stock": quantity})

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
