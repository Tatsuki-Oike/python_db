from pymongo import MongoClient

# MongoDBに接続
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # データベース名を指定
collection = db["mycollection"]  # コレクション名を指定

def find_data(query):
    print("---------------------------------------")
    print("find", query)
    result = collection.find(query) # ドキュメントを取得
    for doc in result: # ドキュメントを表示
        print(doc)

# 複数CREATE
data_to_insert = [
    {"name": "Ichiro", "age": 25},
    {"name": "Jiro", "age": 30},
    {"name": "Saburo", "age": 35}
]
result = collection.insert_many(data_to_insert)

# READ
find_data(None)

query = {"name": "Jiro"} # 等しい
find_data(query)

query = {"name": {"$ne": "Jiro"}} # 等しくない
find_data(query)

query = {"age": {"$gt": 30}} # age > 30
find_data(query)

query = {"age": {"$gte": 30}} # age >= 30
find_data(query)

query = {"age": {"$lt": 30}} # age < 30
find_data(query)

query = {"age": {"$lte": 30}} # age <= 30
find_data(query)

query = {"name": {"$in": ["Jiro", "Saburo"]}}
find_data(query)

# DELETE
collection.delete_many({})