from pymongo import MongoClient

# 1 MongoDBに接続
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # データベース名を指定
collection = db["mycollection"]  # コレクション名を指定


# 2 CRUD

## CREATE
data = {
    "name": "Ichiro",
    "age": 30,
    "city": "Tokyo",
    "item_data": ["item1", "item2"]
    }
collection.insert_one(data)

## READ
print("----------------------------------------------")
print("READ")
result = collection.find() # ドキュメントを取得
for doc in result: # ドキュメントを表示
    print(doc)

## UPDATE
query = {"name": "Ichiro"} # 更新対象の条件を指定
new_data = {"$set": {"age": 25}} # 更新内容を指定
collection.update_one(query, new_data) # ドキュメントを更新

print("----------------------------------------------")
print("UPDATE")
result = collection.find() # ドキュメントを取得
for doc in result: # ドキュメントを表示
    print(doc)

## DELETE
query = {"name": "Ichiro"} # 削除対象の条件を指定
collection.delete_one(query) # ドキュメントを削除

print("----------------------------------------------")
print("DELETE")
result = collection.find() # ドキュメントを取得
for doc in result: # ドキュメントを表示
    print(doc)


# 3 複数データ

## 複数CREATE
data_to_insert = [
    {
    "name": "Jiro",
    "age": 20,
    "city": "Kyoto",
    "item_data": ["item3", "item4"]
    },
    {
    "name": "Saburo",
    "age": 32,
    "city": "Tokyo",
    "item_data": ["item5", "item6"]
    }
]
result = collection.insert_many(data_to_insert)

## 複数READ
print("----------------------------------------------")
print("READ")
result = collection.find() # ドキュメントを取得
for doc in result: # ドキュメントを表示
    print(doc)

## DELETE
collection.delete_many({})