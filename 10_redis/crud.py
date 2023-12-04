import redis

r = redis.StrictRedis(host="localhost", port=6379, db=0) # Redisに接続

# 1 CRUD

## CREATE
r.set("key1", "value1") # One
data = {
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
}
r.mset(data) # Multi

## READ One
print("------------------------------------")
print("READ One")
print("READ", r.get("key1"))
print("READ (DECODE)", r.get("key1").decode("utf-8"))

## READ Multi
print("------------------------------------")
print("READ Multi")
all_keys = r.keys("*")
for key in all_keys:
    key_str = key.decode("utf-8")
    value = r.get(key_str).decode('utf-8')
    print(f"キー: {key_str}, 値: {value}")

## Update
print("------------------------------------")
print("Update")
r.set("key1", "value1_change") # UPDATE
print(r.get("key1")) # READ

## Delete
print("------------------------------------")
print("Delete")
r.delete("key1") # DELETE
print(r.get("key1")) # READ


# 2 CRUD List

## CREATE
r.rpush("my_list", "item1") # CREATE One
r.rpush("my_list", "item2") # CREATE One
list_data = ["item3", "item4"] # CREATE Multi
r.rpush("my_list", *list_data)

## READ
print("------------------------------------")
print("READ List")
items = r.lrange("my_list", 0, -1)  # すべての要素を取得
print(items)

## UPDATE
print("------------------------------------")
print("UPDATE List")
r.lset("my_list", 1, "new_item")
items = r.lrange("my_list", 0, -1)  # すべての要素を取得
print(items)

## DELETE
print("------------------------------------")
print("DELETE List")
r.delete("my_list")
items = r.lrange("my_list", 0, -1)  # すべての要素を取得
print(items)


# 3 CRUD Dict

## CREATE
r.hset("my_hash", "field1", "value1") # CREATE One
r.hset("my_hash", "field2", "value2") # CREATE One
data_dict = {
    "field3": "value3",
    "field4": "value4"
}
r.hset("my_hash", mapping=data_dict) # CREATE Multi

## READ
print("------------------------------------")
print("READ Dict")
value = r.hget("my_hash", "field1") # 特定の値を取得
all_data = r.hgetall("my_hash") # すべて取得
print("READ DICT", all_data)

## UPDATE
print("------------------------------------")
print("UPDATE Dict")
r.hset("my_hash", "field1", "new_value")
all_data = r.hgetall("my_hash") # すべて取得
print("READ DICT", all_data) 

## DELETE
print("------------------------------------")
print("DELETE Dict")
r.delete("my_hash")