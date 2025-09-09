from fastapi import FastAPI

app = FastAPI(title="Weather AI API", version="0.1.0")

@app.get("/health")
def health():
	return {"status": "ok"}

@app.get("/version")
def version(): 
	return {"version": "0.1.1", "by": "second-account"}