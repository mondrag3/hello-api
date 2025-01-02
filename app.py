from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()

# Define the ping endpoint
@app.get("/ping")
def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    import uvicorn
    # Run the application
    uvicorn.run(app, host="127.0.0.1", port=8000)
