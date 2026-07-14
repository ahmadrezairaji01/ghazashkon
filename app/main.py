from fastapi import FastAPI

app = FastAPI(
    title="Ghazashkon API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Hello FastAPI!"}