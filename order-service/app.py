# Order Service (order-service/app.py)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    product_id = data.get('product_id')
    
    # Communicate with product service
    try:
        product_response = requests.get(f"http://product-service/product/{product_id}")
        product_data = product_response.json()
    except Exception as e:
        return jsonify({'error': 'Could not fetch product info', 'details': str(e)}), 500

    return jsonify({
        'message': 'Order created',
        'product': product_data
    })

@app.route('/health')
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
