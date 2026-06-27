import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

secret_user: str = "user"
secret_password: str = "pass?"

basic: HTTPBasicCredentials = HTTPBasic()

@app.get("/who")
def get_user(creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if creds.username == secret_user and creds.password == secret_password:
        return {"username": creds.username, "password": creds.password}
    raise HTTPException(status_code=401, detail="Руки на стол, пёс!")

if __name__ == "__main__":
    uvicorn.run("auth:app", reload=True)