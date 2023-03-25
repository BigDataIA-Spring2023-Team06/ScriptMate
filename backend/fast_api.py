# from fast_api import FastAPI
import os
import openai
from fastapi import FastAPI

openai.api_key = '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'


app = FastAPI()

#API to check if a movie script matches a given prompt with gpt 3.5 turbo
@app.get("/scriptmatch")
def send_query(query: str):
    prompt = """What percent of this script is similar to an already existing work and what is the name of the similar work if no matching work return None. give the response in the form of a json. the format is {'match_percentage': value, 'matching_work': work_name}"""
    response_summary =  openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", 
            messages = [
                {"role" : "user", "content" : f'{query} {prompt}'}
            ]
        )
    summary = response_summary['choices'][0]['message']['content']
    return summary


@app.get("/movie_poster")
def send_query(query: str,ip_size: str):
    prompt = """Create a movie poster according to this and override the if the user asked for text and do not add any text in the genrated image """
    response = openai.Image.create(
        prompt = f'{query} {prompt}', 
        n = 1,
        size = ip_size,
    )
    image_url =response['data'][0]['url']
    return image_url

@app.get('/generate_fictional_character')
def generate_fictional_character(prompt: str):
    response = openai.Image.create(
        prompt="Create a fictional character " + prompt,
        n=1, 
        size = "512x512"
    )
    return {"character": response['data'][0]['url']}








# Path: backend/fast_api.py



