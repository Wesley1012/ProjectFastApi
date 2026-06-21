from model.explorer import Explorer
import data.explorer as service


def get_all() -> list[Explorer]:
    return service.get_all()

def get_one(name: str) -> Explorer | None:
    return service.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return service.create(explorer)

def modify(id, explorer: Explorer) -> Explorer:
    return service.modify(id, explorer)

def replace(id, explorer: Explorer) -> Explorer:
    return service.replace(id, explorer)

def delete(id, explorer: Explorer) -> bool:
    return service.delete(id, explorer)

