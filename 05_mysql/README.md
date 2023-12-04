# コンテナ(環境)の準備

```sh
docker-compose up -d
docker-compose exec mysql bash
```

# Pythonの仮想環境構築

```sh
cd /code
python3 -m venv venv # 仮想環境作成
source venv/bin/activate # 環境の中にはいる
python3 -m pip install --upgrade pip # pip upgrade
pip3 install -r requirements.txt # ライブラリインストール
```

# Pythonの実行

```python
python run.py
```


# コンテナの消去

```sh
exit
docker-compose down
```