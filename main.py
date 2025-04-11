from fastapi import FastAPI
from controller.abb_controller import router as pet_router

app = FastAPI()
app.include_router(pet_router)

@app.get("/")
def root():
    return {"message": "API de Mascotas corriendo correctamente"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

