from fastapi import FastAPI

app = FastAPI(title="${{ values.name }}")

@app.get("/")
def read_root():
    return {"message": "Hello from ${{ values.name }}"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}