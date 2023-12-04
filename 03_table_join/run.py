import sqlite3
import datetime
import pandas as pd

def main():

    con = sqlite3.connect("sample.db") # ファイル読み込み
    cur = con.cursor()

    make_table(cur, con) # CREATE TABLE
    join_table(con)

    cur.execute("DROP TABLE user_table")
    cur.execute("DROP TABLE item_table")
    cur.execute("DROP TABLE purchase_table")
    con.commit() # sql実行
    con.close() # DBとの接続閉じる


def sql_result(sql_text, con, column_flg=False):
    print(f"「{sql_text}」") # sql表示
    df = pd.read_sql_query(sql_text, con) # df変換
    if column_flg:
        print(df.columns)
    print(df) # 結果表示

def make_table(cur, con):

    print("--------------------------------------")
    print("user_table")

    cur.execute("""
                CREATE TABLE user_table(
                user_id INTEGER PRIMARY KEY,
                user_name TEXT UNIQUE NOT NULL
                )
                """)
    
    users_list = [(0, "Ichiro"), (1, "Jiro"), (2, "Saburo"), (3, "Shiro")]
    cur.executemany(f"INSERT INTO user_table VALUES(?, ?)", users_list)
    sql_result("SELECT * FROM user_table", con)
    
    print("--------------------------------------")
    print("item_table")
    
    cur.execute("""
                CREATE TABLE item_table(
                item_id INTEGER PRIMARY KEY,
                item_name TEXT UNIQUE NOT NULL,
                item_price INTEGER CHECK( item_price >= 0),
                description TEXT DEFAULT 'no description'
                )
                """)
    
    items_list = [(0, "book", 1000, None), 
                  (1, "water", 100, "You can drink"),
                  (2, "snack", 150, None)]
    for id, name, price, description in items_list:
        if not description:
            cur.execute(f"""
                        INSERT INTO item_table (item_id, item_name, item_price)
                        VALUES({id}, '{name}', {price})
                        """)
        else:
            cur.execute(f"""
                        INSERT INTO item_table (item_id, item_name, item_price, description)
                        VALUES({id}, '{name}', {price}, '{description}')
                        """)
    sql_result("SELECT * FROM item_table", con)


    print("--------------------------------------")
    print("purchase_table")

    cur.execute("""
                CREATE TABLE purchase_table(
                purchase_id INTEGER PRIMARY KEY,
                user_id INTEGER, 
                item_id INTEGER, 
                created_time TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES user_table(user_id),
                FOREIGN KEY (item_id) REFERENCES item_table(item_id)
                )
                """)

    purchases_list = [(0, 0, 1, str(datetime.datetime.now())), 
                  (1, 1, 2, str(datetime.datetime.now())),
                  (2, 1, 1, str(datetime.datetime.now())),
                  (3, 5, 1, str(datetime.datetime.now()))]
    cur.executemany(f"INSERT INTO purchase_table VALUES(?, ?, ?, ?)", purchases_list)
    sql_result("SELECT * FROM purchase_table", con)

def join_table(con):

    print("--------------------------------------")
    print("(INNER) JOIN table")

    sql_text = """
    SELECT * 
    FROM purchase_table
    JOIN user_table
    ON purchase_table.user_id = user_table.user_id
    """
    sql_result(sql_text, con)

    print("--------------------------------------")
    print("(INNER) JOIN table ✖️ 2")

    sql_text = """
    SELECT * 
    FROM purchase_table
    JOIN user_table
    ON purchase_table.user_id = user_table.user_id
    JOIN item_table
    ON purchase_table.user_id = item_table.item_id
    """
    sql_result(sql_text, con, True)

    print("--------------------------------------")
    print("LEFT (OUTER) JOIN table")

    sql_text = """
    SELECT * 
    FROM purchase_table
    LEFT JOIN user_table
    ON purchase_table.user_id = user_table.user_id
    """
    sql_result(sql_text, con)

    print("--------------------------------------")
    print("RIGHT (OUTER) JOIN table")

    sql_text = """
    SELECT * 
    FROM purchase_table
    RIGHT JOIN user_table
    ON purchase_table.user_id = user_table.user_id
    """
    sql_result(sql_text, con)

    print("--------------------------------------")
    print("FULL (OUTER) JOIN table")

    sql_text = """
    SELECT * 
    FROM purchase_table
    FULL JOIN user_table
    ON purchase_table.user_id = user_table.user_id
    """
    sql_result(sql_text, con)

if __name__ == "__main__":
    main()
