from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso"}

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a - b}