# FastAPI

FastAPI is a modern and fast web framework for building APIs with **Python**. It allows developers to create web applications and services quickly and easily.

Think of FastAPI as a tool that helps your machine learning model talk to the outside world — like a bridge between your code and users.

Some feature of FastAPI are:

- **Fast**: It’s designed to be super quick.
- **Easy to Use**: The code is clean and simple.
- **Automatic Docs**: It creates interactive documentation automatically.
- **Data Validation**: It checks if the input data is correct, so your model won’t crash.

### Why is FastAPI Important for Machine Learning?

When you train a machine learning model, it usually runs on your computer and makes predictions for you. But what if you want others to use it?

That’s where **FastAPI** comes in. It lets you:

1. **Deploy your model** as a web service.
2. **Send data to your model** over the internet (like from a website or app).
3. **Get predictions** in real time.

### Installing FastApi

To install fasapi you can execute the following command

```bash
uv add fastapi
```

# What is Uvicorn and Why is it Needed with FastAPI?

**Uvicorn** is a **web server** that runs your **FastAPI** app. Think of it like the engine that powers your API and allows people to actually connect to it and use it.

FastAPI is the **code** you write (like the brain of your app), and Uvicorn is the **tool that runs it and makes it available on the web**.

---

## Analogy: A FastAPI Restaurant

Imagine you opened a restaurant (your machine learning API):

- **FastAPI** is like the chef. It knows how to prepare the meals (make predictions).
- **Uvicorn** is like the front door and waitstaff. It lets customers in, takes their orders, and delivers the meals.

Without Uvicorn:

- Your chef is ready, but no one can enter the restaurant or place an order.

With Uvicorn:

- The restaurant opens, customers come in, and the chef starts cooking!

## Run FastAPI File and Make a Request

To run the FastApi application `api.py`, that exposes two endpoints (/get_fraction and /post_fraction), using uvicorn you can execute the following command:

```bash
uv run python -m uvicorn content.model_deployment.fastapi.api:app
```

You can test the endpoint get_fraction of the api.py using the following command:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/get_fraction?a=2&b=2' \
  -H 'accept: application/json'
```

You can test the endpoint post_fraction of the api.py using the following command:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/post_fraction' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"a": 2, "b": 2}'
```

To run the FastApi application fastapi_pydantic.py which uses pydatin to validate input and output data,you can execute the following command:

```bash
uv run python content/model_deployment/fastapi/fastapi_pydantic.py
```
