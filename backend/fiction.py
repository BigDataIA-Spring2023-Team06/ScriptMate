import openai
from fastapi import FastAPI

# Set up OpenAI API credentials
openai.api_key = "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"
model_engine = "dall-e-chat-3"

# Create FastAPI app
app = FastAPI()

# Define API endpoint
@app.get('/generate_fictional_character')
def generate_fictional_character(prompt: str):
    response = openai.Image.create(
        prompt="Create a fictional character " + prompt,
        n=1, 
        size = "512x512"
    )
    return {"character": response['data'][0]['url']}

# # Run FastAPI app
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, host='0.0.0.0', port=8000)
