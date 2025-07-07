from fastapi import FastAPI

app = FastAPI(
    title="${{ values.name }}",
    description="${{ values.description }}",
    version="1.0.0"
)


@app.get("/")
def read_root():
    return {
        "message": "Hello from ${{ values.name }}",
        "service": "${{ values.name }}",
        "description": "${{ values.description }}"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "${{ values.name }}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
