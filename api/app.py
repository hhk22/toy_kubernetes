from fastapi import FastAPI
import requests
import re

app = FastAPI()

def encode_url(url):
    return re.sub(r"[\.\,\/:]", "", url)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/scrape")
async def scape(url: str):
    encoded_url = encode_url(url)
    path = f"/api/dynamic-vol/html/{encoded_url}.txt"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    with open(path, "w", encoding="utf-8") as f:
        html = requests.get(url, headers=headers).text
        print("path", path)
        f.write(html)
        return path
    
@app.get("/test")
async def test():
    return "HI"