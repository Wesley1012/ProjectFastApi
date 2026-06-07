import uvicorn
from fastapi import FastAPI, Body, Header, Response, Depends, Query
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse,\
                              RedirectResponse, FileResponse, StreamingResponse


app = FastAPI()

@app.get('/')
def home():
    return {"message": "Zdarova, zaebal!"}

@app.post('/hi')
def hello(name: str = Body(embed=True)):
    return f"Hello, {name}"

@app.post("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent

@app.get("/happy")
def happy(statuse_code: int =200):
    return "4inazes"

@app.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    response.headers[name] = value
    return "normal body"

def user_dep(name: str = Query(..., description="Имя пользователя"),
             password: str = Query(..., description="Пароль")):
    return {"name": name, "valid": True}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

def check_dep(name: str = Query(..., description="Имя пользователя"),
             password: str = Query(..., description="Пароль")):
    if not name:
        raise

@app.get("/check_user", description=[Depends(check_dep())])
def check_user() -> bool:
    return True

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000, reload=True)