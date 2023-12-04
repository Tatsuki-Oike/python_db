import mysql.connector
import pandas as pd

# MySQL接続設定
config = {
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "database": "your_database_name",
    "raise_on_warnings": True
}

def main():

    con = mysql.connector.connect(**config)
    cur = con.cursor()

    sql_execute(cur, con) # SQL実行

    con.commit() # sql実行
    con.close() # DBとの接続閉じる

def sql_execute(cur, con):

    sql_text = """
    CREATE TABLE students(
        id INT,
        japanese INT,
        english INT,
        math INT)
    """
    cur.execute(sql_text) # CREATE TABLE

    cur.execute("INSERT INTO students VALUES(0, 50, 30, 20)") # データ追加
    print("「SELECT * FROM students」")
    df = pd.read_sql_query("SELECT * FROM students", con) # df変換
    print(df) # 表示
    
    cur.execute("DROP TABLE students") # DELETE TABLE

if __name__ == "__main__":
    main()
