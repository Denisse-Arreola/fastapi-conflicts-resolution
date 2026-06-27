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
    return {"Hello": "World Melanie"}
