from openai import OpenAI
import os
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from fastapi.staticfiles import StaticFiles
import base64

templates = Jinja2Templates(directory="templates")

web = FastAPI()
web.mount("/static", StaticFiles(directory="static"), name="static")

def generate_image(prompt):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url

@web.get("/", response_class=HTMLResponse)
async def first(req: Request):
    return templates.TemplateResponse("index.html", {"request": req})

@web.post("/image")
async def image(component: str = Form(...)):
    flag = False
    url = generate_image(component)
    image_data = requests.get(url).content
    output = os.path.join("static","dalleimg.jpg") # Save image with a fixed filename
    with open(output, "wb") as file:
        file.write(image_data)
    flag = True
    print(output)
    return {"flag": flag, "src": output}