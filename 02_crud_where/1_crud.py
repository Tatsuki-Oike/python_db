import sqlite3
import pandas as pd

def main():

    con = sqlite3.connect("sample.db") # ファイル読み込み
    cur = con.cursor()

    make_table(cur, con) # CREATE TABLE
    crud(cur, con) # SQL実行

    cur.execute("DROP TABLE students") # DELETE TABLE
    con.commit() # sql実行
    con.close() # DBとの接続閉じる

def sql_result(sql_text, con):
    print(f"「{sql_text}」") # sql表示
    df = pd.read_sql_query(sql_text, con) # df変換
    print(df) # 結果表示

def make_table(cur, con):

    cur.execute("CREATE TABLE students(id, japanese, english, math, year)") # CREATE TABLE

    # データ追加
    students_df = pd.read_csv("../01_python_sqlite/students.csv")
    students_df.to_sql("students", con, if_exists="append", index=None)
    sql_result("SELECT * FROM students", con)

def crud(cur, con):
    
    print("--------------------------------------")
    print("CREATE")
    print(f"「INSERT INTO students VALUES(10, 75, 75, 75, 'M2')」")
    cur.execute(f"INSERT INTO students VALUES(10, 75, 75, 75, 'M2')")

    print("--------------------------------------")
    print("READ")
    sql_result("SELECT * FROM students WHERE math>70", con)

    print("--------------------------------------")
    print("UPDATE")
    print("「UPDATE students SET japanese=90 WHERE id=1」")
    cur.execute("UPDATE students SET japanese=90 WHERE id=1")

    print("--------------------------------------")
    print("DELETE")
    print("「DELETE FROM students WHERE id=3」")
    cur.execute("DELETE FROM students WHERE id=3")

    print("--------------------------------------")
    sql_result("SELECT * FROM students", con)

if __name__ == "__main__":
    main()
