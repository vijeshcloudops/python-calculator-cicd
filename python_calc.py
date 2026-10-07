from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
<head>
    <title>SimpleCalc</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 40px auto; background: #f7f9fa;}
        h2 { color: #2A5676; }
        form { margin-bottom: 20px; }
        input, select { padding: 6px; margin-right: 4px; }
        button { padding: 6px 16px; }
        .error { color: #b10000; }
    </style>
</head>
<body>
    <h2>Simple Calculator</h2>
    <form method="post">
      <input name="a" type="number" step="any" required placeholder="First number">
      <select name="op">
        <option value="+">+</option>
        <option value="-">−</option>
        <option value="*">×</option>
        <option value="/">÷</option>
      </select>
      <input name="b" type="number" step="any" required placeholder="Second number">
      <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
      {% if error %}
        <p class="error">Error: <strong>{{ result }}</strong></p>
      {% else %}
        <p>Result: <strong>{{ result }}</strong></p>
      {% endif %}
    {% endif %}
</body>
</html>
"""

def calculate(a, b, op):
    """Perform calculation with full validation and error handling."""
    VALID_OPS = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}
    
    # Input validation
    try:
        a = float(a)
        b = float(b)
    except (TypeError, ValueError):
        return "Inputs must be valid numbers", True

    # Operator validation
    if op not in VALID_OPS:
        return "Unknown operation", True

    # Division by zero
    if op == "/" and b == 0:
        return "Division by zero is not allowed", True

    # Perform calculation
    try:
        if op == "+":
            return str(a + b), False
        elif op == "-":
            return str(a - b), False
        elif op == "*":
            return str(a * b), False
        elif op == "/":
            return str(a / b), False
    except Exception as exc:
        return "Internal calculation error", True

    return "Unhandled operation", True

@app.route("/", methods=["GET", "POST"])
def calc():
    result = None
    error = False
    if request.method == "POST":
        a = request.form.get("a")
        b = request.form.get("b")
        op = request.form.get("op")
        result, error = calculate(a, b, op)
    return render_template_string(HTML, result=result, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
