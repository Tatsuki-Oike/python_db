import sqlite3
import pandas as pd

def main():

    con = sqlite3.connect("sample.db") # ファイル読み込み
    cur = con.cursor()

    make_table(cur, con) # CREATE TABLE
    execute_sql(con) # SQL実行

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

def execute_sql(con):
    
    print("--------------------------------------")
    # %は任意の0文字以上, _は任意の1文字
    sql_text = "SELECT * FROM students WHERE year LIKE 'M_'"
    sql_result(sql_text, con)

    print("--------------------------------------")
    sql_text = "SELECT * FROM students WHERE math BETWEEN 30 AND 60"
    sql_result(sql_text, con)

    print("--------------------------------------")
    sql_text = "SELECT * FROM students WHERE year IN ('B4', 'M1')"
    sql_result(sql_text, con)

    print("--------------------------------------")
    sql_text = "SELECT * FROM students WHERE year NOT IN ('B4', 'M1')"
    sql_result(sql_text, con)

    print("--------------------------------------")
    sql_text = """
    SELECT * FROM students 
    WHERE math > 50
    AND english > 50
    """
    sql_result(sql_text, con)

    print("--------------------------------------")
    sql_text = """
    SELECT * FROM students 
    WHERE math > 50
    OR english > 50
    """   
    sql_result(sql_text, con)

if __name__ == "__main__":
    main()
