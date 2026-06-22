from data.init import conn, curs, IntegrityError
from model.creature import Creature
from errors import Missing, Duplicate

curs.execute("""create table if not exists creature(
                name text primary key,
                description text,
                country text,
                area text,
                aka text)""")

def row_to_model(row: tuple) -> Creature:
    if row is None:
        return None
    name, description, country, area, aka = row
    return Creature(name=name,
                    description=description,
                    country=country,
                    area=area,
                    aka=aka)

def model_to_dict(creature: Creature) -> dict:
    return creature.dict()

def get_one(name: str) -> Creature:
    qry = "select * from creature where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Creature {name} not found")


def get_all() -> list[Creature]:
    qry = "select * from creature"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]

def create(creature: Creature):
    qry = """insert into creature (name, description, country, area, aka)
     values (:name, :description, :country, :area, :aka)"""
    params = model_to_dict(creature)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=
                        f"Creature {creature.name} already exists")
    return get_one(creature.name)

def modify(name: str, creature: Creature):
    qry = """update creature
               set name=:name,
                   country=:country,
                   area=:area,
                   description=:description,
                   aka=:aka
               where name=:old_name"""
    params = model_to_dict(creature)
    params["old_name"] = name

    curs.execute(qry, params)
    if curs.rowcount == 0:
        raise Missing(msg=f"Creature {name} not found")
    return get_one(creature.name)


# def replace(creature: Creature):
#     return creature

def delete(name: str):
    qry = "delete from creature where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"Creature {name} not found")