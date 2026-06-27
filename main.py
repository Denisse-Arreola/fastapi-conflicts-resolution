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
    return {"Hello": "Welcome :)"}
