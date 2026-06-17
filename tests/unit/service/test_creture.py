from model.creature import Creature
from service import creature as code

sample = Creature(name="Yeti",
                  country="CN",
                  area="Himalayas",
                  description="Hirsute Himalayan",
                  aka="Abominable Showman",
                  )

def test_creaature():
    resp = code.create(sample)
    assert resp == sample

def test_get_exists():
    resp = code.get_one("Yeti")
    assert resp == sample

def test_get_missing():
    resp = code.get_one("Azzazin")
    assert resp == None