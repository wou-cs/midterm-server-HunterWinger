from flask import Flask, request

app = Flask(__name__)

@app.route("/api/calcs/<value>")
def calculate(value):
    # Ensure that our number isn't negative 
    try:
        number = int(value)
        if number <= 0:
            raise ValueError
    except ValueError:
        return "Invalid input", 400

    # Construct our JSON string
    response = (
        '{'
        # Number - 1 and format into hex using string interp
        f'"dec": {number - 1}, '
        f'"hex": "0x{number:x}"'
        '}'
    )

    return response, 200, {"Content-Type": "application/json"}

if __name__ == "__main__":
    app.run(port=8080)
