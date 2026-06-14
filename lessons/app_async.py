from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get('/hi')
async def hello(name):
    await asyncio.sleep(1)
    return f"Hello, {name}"

if __name__=="__main__":
    uvicorn.run('app_async;app')