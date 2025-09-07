from fastapi import FastAPI

app = FastAPI(title="Sample API", version="0.1.0")

@app.get("/test")
def read_test():
    return {"status": "ok", "message": "Test endpoint working"}
