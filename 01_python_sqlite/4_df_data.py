import sqlite3
import pandas as pd

def main():

    con = sqlite3.connect("sample.db") # ファイル読み込み
    cur = con.cursor()

    sql_execute(cur, con) # SQL実行

    con.commit() # sql実行
    con.close() # DBとの接続閉じる

def sql_result(sql_text, con):
    print(f"「{sql_text}」") # sql表示
    df = pd.read_sql_query(sql_text, con) # df変換
    print(df) # 結果表示

def sql_execute(cur, con):
    
    cur.execute("CREATE TABLE students(id, japanese, english, math, year)") # CREATE TABLE

    # データ追加
    students_df = pd.read_csv("students.csv")
    students_df.to_sql("students", con, if_exists="append", index=None)
    sql_result("SELECT * FROM students", con)

    cur.execute("DROP TABLE students") # DELETE TABLE

if __name__ == "__main__":
    main()
