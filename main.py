from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/harga')
def get_harga():
    return jsonify({
        'BTC': {'current': 67420 + random.randint(-1000, 1000), 'change': round(random.uniform(-5, 5), 2), 'history': [65800, 66200, 65900, 66800, 67100, 67000, 67420]},
        'ETH': {'current': 3245 + random.randint(-100, 100), 'change': round(random.uniform(-3, 3), 2), 'history': [3180, 3200, 3190, 3220, 3235, 3240, 3246]},
        'SOL': {'current': 142 + random.randint(-10, 10), 'change': round(random.uniform(-2, 2), 2), 'history': [145, 144, 143, 144, 143, 142, 142]},
        'XRP': {'current': 0.52 + random.uniform(-0.05, 0.05), 'change': round(random.uniform(-3, 3), 2), 'history': [0.505, 0.510, 0.512, 0.518, 0.520, 0.521, 0.523]},
        'MATIC': {'current': 0.89 + random.uniform(-0.05, 0.05), 'change': round(random.uniform(-2, 2), 2), 'history': [0.880, 0.885, 0.882, 0.888, 0.891, 0.893, 0.895]}
    })

@app.route('/api/sinyal')
def get_sinyal():
    return jsonify({
        'BTC': {'signal': 'BUY', 'confidence': 0.85, 'reason': 'Momentum positif', 'rsi': 68.4},
        'XRP': {'signal': 'BUY', 'confidence': 0.78, 'reason': 'Breakout resistance', 'rsi': 72.1},
        'SOL': {'signal': 'HOLD', 'confidence': 0.65, 'reason': 'Sideways', 'rsi': 55.3}
    })

@app.route('/api/ledger')
def get_ledger():
    return jsonify({
        'entries': [
            {'date': '2025-11-01', 'action': 'BUY BTC', 'amount': '0.05', 'price': '$67,200', 'note': 'Entry point AI'},
            {'date': '2025-10-28', 'action': 'SELL ETH', 'amount': '1.2', 'price': '$3,180', 'note': 'Take profit 15%'}
        ]
    })

@app.route('/api/ayao')
def get_ayao():
    return jsonify({
        'pools': [
            {'name': 'BTC-USDT', 'apy': 12.5, 'risk': 'Low', 'tvl': '$2.5B', 'minDeposit': 0.01, 'riskFactor': 0.1},
            {'name': 'ETH-USDT', 'apy': 15.2, 'risk': 'Medium', 'tvl': '$1.8B', 'minDeposit': 0.05, 'riskFactor': 0.2}
        ]
    })

@app.route('/api/alerts')
def get_alerts():
    return jsonify({
        'critical': [{'coin': 'BTC', 'price': 70000, 'type': 'resistance', 'urgency': 'high', 'message': 'BTC mendekati $70K!'}],
        'warnings': []
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
