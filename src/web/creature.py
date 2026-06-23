from fastapi import APIRouter
from model.creature import Explorer
import service.creature as service

router = APIRouter(prefix = "/creature")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name) -> Explorer | None:
    return service.get_one(name)

#Остальные точки пока ничего не делают:
@router.post("/")
def create(creature: Explorer) -> Explorer:
    return service.create(creature)

@router.patch("/")
def modify(creature: Explorer) -> Explorer:
    return service.modify(creature)

@router.put("/")
def replace(creature: Explorer) -> Explorer:
    return service.replace(creature)

@router.delete("/{name}")
def delete(name: str):
    return None