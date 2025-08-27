from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/get_fraction")
def get_fraction(a: float, b: float) -> Dict:

    result = a / b
    return {"result": result}


@app.post("/post_fraction")
def post_fraction(data: Dict[str, float]) -> Dict:
    a = data.get("a")
    b = data.get("b")

    result = a / b
    return {"result": result}
