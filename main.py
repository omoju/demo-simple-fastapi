from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="Hello World API",
    description="A simple FastAPI demo that returns Hello World",
    version="0.1.0",
    openapi_version="3.0.2"
)

# Define response model for better documentation
class HelloResponse(BaseModel):
    message: str

# Root endpoint
@app.get("/", response_model=HelloResponse, tags=["greeting"])
async def hello_world():
    """
    Returns a simple Hello World message.
    
    Returns:
        HelloResponse: A JSON object containing the greeting message
    """
    return HelloResponse(message="Hello World")

# Health check endpoint
@app.get("/health", tags=["system"])
async def health_check():
    """
    Simple health check endpoint to verify the API is running.
    
    Returns:
        dict: Status information
    """
    return {"status": "healthy"}

# Run the app with uvicorn when this file is executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)