from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/get_fraction")
def get_fraction(a: float, b: float) -> Dict:
    if a is None or b is None:
        return {"error": "Both 'a' and 'b' must be provided."}

    if b == 0:
        return {"error": "Division by zero is not allowed."}

    result = a / b
    return {"result": result}


@app.post("/post_fraction")
def post_fraction(data: Dict[str, float]) -> Dict:
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        return {"error": "Both 'a' and 'b' must be provided."}

    if b == 0:
        return {"error": "Division by zero is not allowed."}

    result = a / b
    return {"result": result}
