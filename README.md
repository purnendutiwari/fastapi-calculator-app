# FastAPI Calculator Microservice


A tiny FastAPI microservice that exposes calculator endpoints and includes unit + integration tests and a GitHub Actions workflow.


## Endpoints


- `GET /` - service health
- `GET /calc/add?a=1&b=2` - add two numbers (query params)
- `GET /calc/subtract?a=1&b=2` - subtract
- `GET /calc/multiply?a=2&b=3` - multiply
- `GET /calc/divide?a=4&b=2` - divide (returns 400 on divide-by-zero)


## Run locally


1. Create venv and activate it


```bash
python -m venv .venv
source .venv/bin/activate # Linux/Mac
.venv\Scripts\activate # Windowssss


