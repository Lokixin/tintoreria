from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

meta = MetaData()

clients = Table(
    "clients",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String),
    Column("surname", String),
    Column("phone", String)
)


class AbstractPSQLRepository:
    pass


if __name__ == "__main__":
    path = "postgresql://postgres:rauzaruk@localhost/test"
    engine = create_engine(path, echo=True)
    meta.create_all(engine)
