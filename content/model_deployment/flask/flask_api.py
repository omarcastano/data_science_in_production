from flask import Flask, request

app = Flask(__name__)


# route for welcome message
@app.route("/")
def welcome() -> str:
    """Welcome message"""

    return "This is my first Flask API"


# Basic Example of a Flask API using GET method
@app.route("/get_fraction/<float:a>/<float:b>", methods=["GET"])
def get_fraction(a: float, b: float) -> str:
    """
    Basic example of a Flask API that returns the fraction of two numbers.
    Notice that the output must be a The return type must be a string, dict, list or tuple.
    """

    response = a / b

    return str(response)


# Basic Example of a Flask API using GET method, expecting a dictionary as input and returning a dict as output
@app.route("/get_fraction_dict", methods=["GET"])
def get_fraction_dict() -> dict:
    """
    Basic example of a Flask API that receives a dictionary as input and returns a dictionary as output.
    """

    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    return {"result": a / b}


# Basic Example of a Flask API using POST method
@app.route("/post_fraction", methods=["POST"])
def post_fraction() -> dict:

    a = request.args.get("a", type=float)
    b = request.args.get("b", type=float)

    return {"result": a / b}


if __name__ == "__main__":
    app.run()
