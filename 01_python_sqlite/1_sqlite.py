import sqlite3
import pandas as pd

def main():

    con = sqlite3.connect("sample.db") # ファイル読み込み
    cur = con.cursor()

    sql_execute(cur, con) # SQL実行

    con.commit() # sql実行
    con.close() # DBとの接続閉じる

def sql_execute(cur, con):

    cur.execute("CREATE TABLE students(id, japanese, english, math)") # CREATE TABLE

    cur.execute("INSERT INTO students VALUES(0, 50, 30, 20)") # データ追加
    print("「SELECT * FROM students」")
    df = pd.read_sql_query("SELECT * FROM students", con) # df変換
    print(df) # 表示
    
    cur.execute("DROP TABLE students") # DELETE TABLE

if __name__ == "__main__":
    main()
