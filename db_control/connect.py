from sqlalchemy import create_engine
import os
from pathlib import Path
from dotenv import load_dotenv

# 環境変数の読み込み
base_path = Path(__file__).parents[1]  # backendディレクトリへのパス
env_path = base_path / '.env'
load_dotenv(dotenv_path=env_path)

# データベース接続情報
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

# SSL証明書のパス
ssl_cert = str(base_path / 'DigiCertGlobalRootCA.crt.pem')

# MySQLのURL構築
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# エンジンの作成（SSL設定を追加）
engine = create_engine(
    DATABASE_URL,
    connect_args={
        "ssl": {
            "ssl_ca": ssl_cert
        }
    },
    echo=True,
    pool_pre_ping=True,
    pool_recycle=3600
)

print("Current working directory:", os.getcwd())
print("Certificate file exists:", os.path.exists('DigiCertGlobalRootCA.crt.pem'))

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker  # ← これを追加！
# from sqlalchemy import create_engine, text  # ← text をインポート！
# from dotenv import load_dotenv

# import os
# # uname() error回避
# import platform
# print("platform:", platform.uname())


# # ## SQLite用コード ###

# # main_path = os.path.dirname(os.path.abspath(__file__))
# # path = os.chdir(main_path)
# # print("path:", path)
# # engine = create_engine("sqlite:///CRM.db", echo=True)


# ### MySQL用コード ###

# # 環境変数の読み込み
# load_dotenv()

# # 環境変数の確認
# print("DB_USER:", os.getenv('DB_USER'))  # 確認用
# print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))  # 確認用
# print("DB_HOST:", os.getenv('DB_HOST'))  # 確認用
# print("DB_PORT:", os.getenv('DB_PORT'))  # 確認用
# print("DB_NAME:", os.getenv('DB_NAME'))  # 確認用

# # データベース接続情報
# DB_USER = os.getenv('DB_USER')
# DB_PASSWORD = os.getenv('DB_PASSWORD')
# DB_HOST = os.getenv('DB_HOST')
# DB_PORT = os.getenv('DB_PORT')
# DB_NAME = os.getenv('DB_NAME')

# # MySQLのURL構築
# DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # MySQL へ接続
# try:
#     engine = create_engine(DATABASE_URL, echo=True)
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
#     # DB接続テスト
#     with engine.connect() as conn:
#         result = conn.execute(text("SELECT DATABASE();"))  # ← text() を使う！
#         db_name = result.fetchone()
#         print(f"✅ MySQL に接続成功！現在のデータベース: {db_name[0]}")
    
#     # 🔹 customers テーブルのデータを取得する
#         print("\n📌 customers テーブルのデータを取得中...")
#         result = conn.execute(text("SELECT * FROM customers;"))  # ← `customers` テーブルのデータを取得！
#         rows = result.fetchall()

#         if rows:
#             print("\n✅ 取得したデータ:")
#             for row in rows:
#                 print(row)  # 取得したデータを表示
#         else:
#             print("\n⚠️ `customers` テーブルにはデータがありません！")
            
# except Exception as e:
#     print("❌ MySQL に接続できませんでした！")
#     print(f"エラー内容: {e}")
    
# # エンジンの作成
# engine = create_engine(
#     DATABASE_URL,
#     echo=True,
#     pool_pre_ping=True,
#     pool_recycle=3600
# )
