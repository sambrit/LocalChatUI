import os
import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI()

# Add CORS middleware to allow the frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8080"],  # Frontend address
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Request model for chat endpoint
class ChatRequest(BaseModel):
    prompt: str

@app.post("/chat/")
def chat(request: ChatRequest):
    """
    Endpoint to interact with the AI model.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": request.prompt}]
        )
        return {"response": response.choices[0].message["content"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during AI response: {str(e)}")
