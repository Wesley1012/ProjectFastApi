from model.creature import Creature


_creatures = [
    Creature(name="Yeti",
             aka='Abominable Showman',
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan"),
    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch",
             ),
    ]

def get_all() -> list[Creature]:
    """Возрат всех существ"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Возврат одного существа"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None

#Ниже будут функции без функционала
def create(creature: Creature) -> Creature:
    """Добавление существа"""
    return creature

def modify(creature: Creature) -> Creature:
    """Частичное изменение записи существа"""
    return creature

def replace(creature: Creature) -> Creature:
    """Полная замена записи существа"""
    return creature

def delete(name: str):
    """Удаление записи; возращение None если запись существовала"""
    return None