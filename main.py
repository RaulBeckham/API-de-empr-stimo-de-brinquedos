from fastapi import FastAPI
from api.routes import crianca, brinquedo, emprestimo, emprestimo, emprestimo

app = FastAPI()

app.include_router(crianca.router)
app.include_router(brinquedo.router)
app.include_router(emprestimo.router)

@app.get("/")
def home():
    return {"message": "API online"}
