# Mongodb環境

```sh
docker build -t python-mongodb .
docker run -it --rm -v $(pwd):/code python-mongodb bash
mongod --fork --logpath /var/log/mongodb.log
```

# Pythonの仮想環境構築

```sh
cd /code
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install pymongo # ライブラリインストール
```

# Python実行

```python
python crud.py
python find.py
```