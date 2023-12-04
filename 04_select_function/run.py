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
    
    # DISTINCT
    print("--------------------------------------")
    print("DISTINCT")
    sql_text = "SELECT DISTINCT year FROM students"
    sql_result(sql_text, con)

    # AS
    print("--------------------------------------")
    print("AS")
    sql_text = "SELECT year AS 学年 FROM students"
    sql_result(sql_text, con)

    # ORDER BY
    print("--------------------------------------")
    print("ORDER BY & LIMIT")
    sql_text = "SELECT * FROM students ORDER BY japanese LIMIT 3"
    sql_result(sql_text, con)
    
    print("--------------------------------------")
    print("ORDER BY & DESC")
    sql_text = "SELECT * FROM students ORDER BY japanese DESC LIMIT 3"
    sql_result(sql_text, con)

    # 文字と関数
    print("--------------------------------------")
    print("REPLACE")
    sql_text = "SELECT REPLACE(year, 'M1', 'Master1') AS year FROM students"
    sql_result(sql_text, con)

    print("--------------------------------------")
    print("LENGTH")
    sql_text = """
    SELECT LENGTH(REPLACE(year, 'M1', 'Master1')) AS length 
    FROM students
    """
    sql_result(sql_text, con)

    # 数値と関数
    print("--------------------------------------")
    print("標準偏差")
    sql_text = """
    SELECT ROUND(SQRT(POWER(math - AVG(math), 2)/COUNT(math)), 2) AS std 
    FROM students
    """
    sql_result(sql_text, con)

    # GROUP BY
    print("--------------------------------------")
    print("GROUP BY")
    sql_text = """
    SELECT year, ROUND(AVG(math), 1) AS avg_math FROM students
    GROUP BY year
    """
    sql_result(sql_text, con)

    # GROUP BY HAVING
    print("--------------------------------------")
    print("GROUP BY HAVING")
    sql_text = """
    SELECT year, ROUND(AVG(math), 1) AS avg_math FROM students
    GROUP BY year
    HAVING AVG(math) > 50
    """
    sql_result(sql_text, con)

    # 副問い合わせ
    print("--------------------------------------")
    print("副問い合わせ")
    sql_text = """
    SELECT * FROM students
    WHERE math = (SELECT MAX(math) FROM students)
    """
    sql_result(sql_text, con)

if __name__ == "__main__":
    main()
