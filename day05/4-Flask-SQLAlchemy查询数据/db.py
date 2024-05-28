"""
Create database:
    > create database db_flask_demo_school charset=utf8mb4
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *

db = SQLAlchemy()
