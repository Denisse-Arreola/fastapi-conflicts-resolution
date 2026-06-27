from fastapi import FastAPI

# App Init
app = FastAPI(
    title="API System",
    description="API service to print Hello World",
    version="1.3.2"
)

# Root endpoint
@app.get("/")
def read_root():
<<<<<<< HEAD
    return {"Hello": "Welcome :)"}
=======
    return {"I'm": "Testing"}
>>>>>>> 04720e08f1ffd67786a5d3132aaa34280a472ab6
