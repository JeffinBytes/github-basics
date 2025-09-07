# Sample FastAPI App

## Run locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## Test
- curl: `curl -s http://localhost:8000/test`
