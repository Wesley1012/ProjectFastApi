from model.creature import Explorer
import data.creature as data


def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer | None:
    return data.get_one(name)

def create(creature: Explorer) -> Explorer:
    return data.create(creature)

def modify(id, creature: Explorer) -> Explorer:
    return data.modify(id, creature)

def replace(id, creature: Explorer) -> Explorer:
    return data.replace(id, creature)

def delete(id, creature: Explorer) -> bool:
    return data.delete(id)