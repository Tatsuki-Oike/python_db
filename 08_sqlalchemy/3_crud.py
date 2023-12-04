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

# CREATE
df = pd.read_csv("students.csv")
df.to_sql("students", engine, index=False, if_exists="append")

# READ
print("--------------------------------------")
print("READ")
sql_text = session.query(Student).statement # ALL
sql_result(sql_text)

# UPDATE ONE
print("--------------------------------------")
print("UPDATE ONE")
student = session.query(Student).filter(Student.id==3).first()
student.japanese = 100
session.commit()

# UPDATE 複数
print("--------------------------------------")
print("UPDATE 複数")
students = session.query(Student).filter(Student.year=="M1").all()
for student in students:
    student.year = "Master1"
session.commit()

# DELETE ONE
print("--------------------------------------")
print("DELETE ONE")
student = session.query(Student).filter(Student.id==2).delete()
session.commit()

# DELETE 複数
print("--------------------------------------")
print("DELETE 複数")
student = session.query(Student).filter(Student.year=="M2").delete()
session.commit()

# READ
print("--------------------------------------")
print("READ")
sql_text = session.query(Student).statement # ALL
sql_result(sql_text)

# DELETE ALL
session.query(Student).delete()

# Session finish
session.commit()
session.close()