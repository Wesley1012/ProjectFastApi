from model.creature import Explorer


_creatures = [
    Explorer(name="Yeti",
             aka='Abominable Showman',
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan"),
    Explorer(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch",
             ),
    ]

def get_all() -> list[Explorer]:
    """Возрат всех существ"""
    return _creatures

def get_one(name: str) -> Explorer | None:
    """Возврат одного существа"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

#Ниже будут функции без функционала
def create(creature: Explorer) -> Explorer:
    """Добавление существа"""
    return creature

def modify(creature: Explorer) -> Explorer:
    """Частичное изменение записи существа"""
    return creature

def replace(creature: Explorer) -> Explorer:
    """Полная замена записи существа"""
    return creature

def delete(name: str):
    """Удаление записи; возращение None если запись существовала"""
    return None