"""
创建新的数据库方便迁移操作
CREATE DATABASE db_flask_migrate CHARSET=utf8mb4;
"""
from flask_migrate import Migrate

migrate = Migrate()
