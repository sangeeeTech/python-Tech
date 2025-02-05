from flask import Flask, request,jsonify

app = Flask(__name__)

menu = [
    {"name": "idly", "price": 30},
    {"name": "dosa", "price": 40},
    {"name": "pongal", "price": 50}
]

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        menu.append(data)
    return jsonify(menu)

if __name__ == '__main__;':
    app.run(debug=True)

    
        

