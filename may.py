from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # טוען את ה-HTML שנמצא בתיקיית templates

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    num1 = data.get("num1")
    num2 = data.get("num2")
    operation = data.get("operation")

    if num1 is None or num2 is None or operation not in ["add", "subtract", "multiply", "divide"]:
        return jsonify({"error": "Invalid input"}), 400

    try:
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return jsonify({"error": "Cannot divide by zero"}), 400
            result = num1 / num2

        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=False)