import os
import pytest
from model.explorer import Explorer
from errors import Missing, Duplicate

os.environ["CRYPTID_SQLITE_DB"] = ":memory:"
from data import explorer

@pytest.fixture()
def sample() -> Explorer:
    return Explorer(name="Jack Black", country="CN",
                    description="Oooh maaan!!")

def test_create(sample: Explorer):
    resp = explorer.create(sample)
    assert resp == sample

def test_creature_duplicate(sample: Explorer):
    with pytest.raises(Duplicate):
        _ = explorer.create(sample)

def test_get_one(sample: Explorer):
    resp = explorer.get_one(sample.name)
    assert resp == sample

def test_get_one_missing(sample: Explorer):
    with pytest.raises(Missing):
        _ = explorer.get_one("Zalupa")

def test_modify(sample: Explorer):
    explorer.country = "Ryazan'"
    resp = explorer.modify(sample.name, sample)
    assert resp == sample

@pytest.mark.parametrize("exp",
                         [Explorer(name="Torch", country="BC", description="Nu kak tam s den'gami"),
                          Explorer(name="Obama", country="JD", description="Chupapi menyanya"),
                          Explorer(name="1337", country="33", description="32424"),
                          Explorer(name="", country="", description="")])
def test_modify_missing(exp: Explorer):
    # exp: Explorer = Explorer(name="Torch", country="BC", description="Nu kak tam s den'gami")
    with pytest.raises(Missing):
        _ = explorer.modify(exp.name, exp)

def test_delete(sample: Explorer):
    resp = explorer.delete(sample.name)
    assert resp is None

def test_delete_missing(sample: Explorer):
    with pytest.raises(Missing):
        _ = explorer.delete(sample.name)