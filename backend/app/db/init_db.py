from app.db.database import engine, Base

from app.models.paper import Paper


def create_tables():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":
    create_tables()