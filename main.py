from fastapi import FastAPI

# App Init
app = FastAPI(
    title="API System",
    description="API service to print Hello World",
    version="1.0.0"
)

# Root endpoint
@app.get("/")
def read_root():
<<<<<<< HEAD
    return {"Qué tal todos"}
=======
    return {"I'm": "Testing"}
>>>>>>> 04720e08f1ffd67786a5d3132aaa34280a472ab6
