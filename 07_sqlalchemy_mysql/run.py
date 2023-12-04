import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd

import config

# MySQL接続設定
USER = config.USER
PASSWORD = config.PASSWORD
HOST = config.HOST
DATABASE = config.DATABASE

# mysql 接続
engine = create_engine(f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}")
Base = declarative_base()

# CREATE TABLE
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    japanese = Column(Integer)
    english = Column(Integer)
    math = Column(Integer)
    year = Column(String(10), nullable=False)

Base.metadata.create_all(engine)

# Session start
Session = sessionmaker(bind=engine)
session = Session()

# INSERT INTO
student = Student(id=1, japanese=50, english=50, math=50, year="B4")
session.add(student)
session.commit()

# SELECT Students
students = session.query(Student).all()
for student in students:
    print(student.id, student.japanese, student.english, student.math, student.year)

# SELECT df
sql_text = session.query(Student).statement
print(sql_text)
df = pd.read_sql_query(sql_text, engine)
print(df)

# DELETE
session.query(Student).delete()

# Session finish
session.commit()
session.close()