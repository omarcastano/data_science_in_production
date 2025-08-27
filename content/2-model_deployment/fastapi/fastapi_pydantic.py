"""FastAPI application with Pydantic for input validation and output formatting."""

from fastapi import FastAPI
from pydantic import BaseModel


class InputData(BaseModel):
    a: float = 5
    b: float = 5


class OutputData(BaseModel):
    result: float


app = FastAPI()


@app.post("/post_fraction")
def post_fraction(data: InputData) -> OutputData:

    a = data.a
    b = data.b

    if a is None or b is None:
        raise ValueError("Both 'a' and 'b' must be provided.")

    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    result = a / b

    return OutputData(result=result)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
