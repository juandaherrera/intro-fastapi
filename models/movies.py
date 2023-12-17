from sqlalchemy import Column, Float, Integer, String

from config.database import Base


# Si queremos tener un solo modelo para Bd y validaciones, podemos usar SQLModel de tiangolo
class MovieBD(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
