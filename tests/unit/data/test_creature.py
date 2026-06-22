import os
import pytest
from model.creature import Creature
from errors import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import creature

@pytest.fixture()
def sample() -> Creature:
    return Creature(name="yeti", country="CN", area="Mahachkala",
                    description="Chupapi Munyanya",
                    aka="48")

def test_create(sample: Creature):
    resp = creature.create(sample)
    assert resp == sample

def test_creature_duplicate(sample: Creature):
    with pytest.raises(Duplicate):
        _ = creature.create(sample)

def test_get_one(sample: Creature):
    resp = creature.get_one(sample.name)
    assert resp == sample

def test_get_one_missing(sample: Creature):
    with pytest.raises(Missing):
        _ = creature.get_one("Zalupa")

def test_modify(sample: Creature):
    creature.area = "Pereulok promejbulok"
    resp = creature.modify(sample.name, sample)
    assert resp == sample

def test_modify_missing():
    thing: Creature = Creature(name="Smurfle", country="RU", area="HZ", description="Some gav", aka="47")
    with pytest.raises(Missing):
        _ = creature.modify(thing.name, thing)

def test_delete(sample: Creature):
    resp = creature.delete(sample.name)
    assert resp is None

def test_delete_missing(sample: Creature):
    with pytest.raises(Missing):
        _ = creature.delete(sample.name)