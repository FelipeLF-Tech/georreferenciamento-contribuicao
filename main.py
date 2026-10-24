from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/workshop/")
def get_workshop():
    numero_de_creditos = 10
    numero_de_creditos = numero_de_creditos + 10
    return {
        "Aula1": "Cliente-Servidor com API",
        "creditos": numero_de_creditos
    }
