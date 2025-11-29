"""FastAPI app exposing calculator endpoints."""

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import Union
from .calculator import add, subtract, multiply, divide

Number = Union[int, float]

app = FastAPI(title="Calculator API")


class CalcResult(BaseModel):
    result: float


@app.get("/", tags=["health"])
async def health():
    return {"status": "ok"}


@app.get("/calc/add", response_model=CalcResult)
async def api_add(a: float = Query(...), b: float = Query(...)):
    return {"result": add(a, b)}


@app.get("/calc/subtract", response_model=CalcResult)
async def api_subtract(a: float = Query(...), b: float = Query(...)):
    return {"result": subtract(a, b)}


@app.get("/calc/multiply", response_model=CalcResult)
async def api_multiply(a: float = Query(...), b: float = Query(...)):
    return {"result": multiply(a, b)}


@app.get("/calc/divide", response_model=CalcResult)
async def api_divide(a: float = Query(...), b: float = Query(...)):
    try:
        res = divide(a, b)
    except ValueError as exc:
        # division by zero, etc.
        raise HTTPException(status_code=400, detail=str(exc))
    # ✅ Make sure this return is here and correctly indented
    return {"result": res}
