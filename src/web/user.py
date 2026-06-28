import os
from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from model.user import User
from errors import Missing, Duplicate

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import user as service
else:
    from service import user as service

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(prefix = "/user")

"""Эта зависимость создаёт сообщение в каталоге "/user/token" из формы с пользователем
 и паролем, и возвращает токен доступа"""
oauth2_dep = OAuth2PasswordBearer(tokenUrl="token")

def unauthed():
    raise HTTPException(status_code=401,
                        detail="Incorrect username or password",
                        headers={"WWW-Authenticate": "Bearer"},
                        )

#К этой точке направляется дюбой вызов, содержащий oauth2_dep():
@router.post("/token")
async def create_access_token(
        form_data: OAuth2PasswordRequestForm = Depends()
):
    """Получение имени ползователя и пароля из формы OAuth, возврат токена доступа"""
    user = service.auth_user(form_data.username, form_data.password)
    if not user:
        unauthed()
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user.username}, expires=expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/token")
def get_access_token(token: str = Depends(oauth2_dep)) -> dict:
    return {"token": token}

# ---- CRUD

@router.get("/")
def get_all() -> list[User]:
    return service.get_all()

@router.get("/{name}")
def get_one(name: str) -> User:
    try:
        service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", status_code=201)
def create(user: User) -> User:
    try:
        return service.create(user)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)

@router.patch("/{name}")
def modify(name: str, user: User) -> User:
    try:
        res = service.modify(name, user)
        if res is None:
            raise HTTPException(status_code=500, detail="Modify returned None")
        return res
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.delete("/{name}")
def delete(name: str) -> None:
    try:
        return service.delete(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)