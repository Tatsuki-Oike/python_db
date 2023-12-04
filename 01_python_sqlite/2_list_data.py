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

    cur.execute("CREATE TABLE students(id, japanese, english, math)") # CREATE TABLE

    # データ追加
    students_list = [(0, 50, 30, 20), (1, 30, 40, 60), (2, 60, 70, 20)]
    cur.executemany("INSERT INTO students VALUES(?, ?, ?, ?)", students_list)
    sql_result("SELECT * FROM students", con)

    cur.execute("DROP TABLE students") # DELETE TABLE
    
if __name__ == "__main__":
    main()
