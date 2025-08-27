# Flask

Flask is a lightweight and flexible Python web framework. It's often called a "microframework" because it provides just the essentials for web development, allowing developers to choose and add other tools as needed. Its primary purpose is to help you build web applications, ranging from simple personal websites to complex web services and APIs.

In the context of machine learning, Flask is commonly used to deploy and serve machine learning models. Once you've trained a machine learning model, Flask allows you to create a web API that users or other applications can interact with. This means you can:

- Create an endpoint: Set up a specific URL (e.g., /predict) where users can send data to your model.

- Receive input: Flask can capture data sent by a user (e.g., through a web form or a JSON request).

- Process with the model: Your Flask application then takes this input, feeds it to your pre-trained machine learning model, and gets a prediction or output.

- Return results: Finally, Flask sends the model's output back to the user, often in a structured format like JSON, which can then be displayed in a web interface or consumed by another application.

## Installing Flask

To install Flask, run the following command:

```bash
uv add flask
```

## Running a Flask App

To launch the Flask application flask_api.py, run:

```bash
uv run flask run src/app/deployment/flask_api.py
```

This will open the app in your web browser.

## Testing the Flask App

The file flask_api.py contains basic examples of a Flask API. Let's test each endpoint:

### GET /get_fraction/<float:a>/<float:b>

To test the GET /get_fraction/<float:a>/<float:b> endpoint, open your browser and navigate to <http://localhost:5000/get_fraction/1.0/2.0>. You should see the response 0.5.

You can also run the following command in the terminal:

```bash
curl http://localhost:5000/get_fraction/1.0/2.0
```

### GET /get_fraction_dict

To test the GET /get_fraction_dict endpoint, open your browser and navigate to <http://localhost:5000/get_fraction_dict?a=1.0&b=2.0>. You should see the response {"result": 0.5}.

You can also run the following command in the terminal:

```bash
curl http://localhost:5000/get_fraction_dict?a=1.0\&b=2.0
```

### POST /post_fraction

To test the POST /post_fraction endpoint, using the following command:

```bash
curl -X POST "http://localhost:5000/post_fraction?a=1.0&b=2.0"
```

Notice that is not possible to test the POST endpoint using the browser, since the browser only supports GET requests.
