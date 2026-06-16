from model.explorer import Explorer

_explorers = [
    Explorer(name="Rayan Gosling",
             country="RU",
             description="Scarce during full moons"),
    Explorer(name="John Smith",
             country="DE",
             description=" Myopic machete man"),
    ]

def get_all() -> list[Explorer]:
    """Возврат всех исследователей"""
    return _explorers

def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None

#Ниже будут функции без функционала
def create(explorer: Explorer) -> Explorer:
    """Добавление исследователя"""
    return explorer

def modify(explorer: Explorer) -> Explorer:
    """Частичное изменение записи исследователя"""
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Полная замена записи"""
    return explorer

def delete(name: str) -> Explorer:
    """Удаление записи; возращение None если запись существовала"""
    return None