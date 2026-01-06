from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "歡迎來到超簡單測試用 API！"

@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({
        "message": "這是測試用 API 的回應",
        "status": "success"
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify({
        "received_data": data,
        "message": "資料已成功接收"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)