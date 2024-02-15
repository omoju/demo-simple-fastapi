import logging
from fastapi import FastAPI

# Configure logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.get("/")
async def root():
    logging.info("Hello World endpoint was called")
    return {"message": "Hello World"}
