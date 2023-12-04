import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, desc, distinct
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

    id = Column(Integer, autoincrement=False, primary_key=True)
    japanese = Column(Integer)
    english = Column(Integer)
    math = Column(Integer)
    year = Column(String(10), nullable=False)

Base.metadata.create_all(engine)

# sql_result
def sql_result(sql_text):
    print(f"「{sql_text}」")
    df = pd.read_sql_query(sql_text, engine)
    print(df)

# Session start
Session = sessionmaker(bind=engine)
session = Session()

# INSERT INTO df
df = pd.read_csv("students.csv")
df.to_sql("students", engine, index=False, if_exists="append")

# SELECT
print("--------------------------------------")
print("ALL")
sql_text = session.query(Student).statement # ALL
sql_result(sql_text)

print("--------------------------------------")
print("Column")
sql_text = session.query(Student.id, Student.japanese).statement # Column
sql_result(sql_text)

print("--------------------------------------")
print("filter")
sql_text = session.query(Student).filter(Student.id==3).statement # filter
sql_result(sql_text)

print("--------------------------------------")
print("filter in")
sql_text = session.query(Student).filter(Student.year.in_(["M1", "B4"])).statement # filter
sql_result(sql_text)

print("--------------------------------------")
print("LIMIT")
sql_text = session.query(Student).limit(3).statement # LIMIT
sql_result(sql_text)

print("--------------------------------------")
print("ORDER BY")
sql_text = session.query(Student).order_by(desc(Student.math)).limit(3).statement # ORDER BY
sql_result(sql_text)

print("--------------------------------------")
print("DISTINCT")
sql_text = session.query(distinct(Student.year)).statement # DISTINCT
sql_result(sql_text)

# DELETE
session.query(Student).delete()

# Session finish
session.commit()
session.close()