from turtle import pos
from config.db import postgres_db
from account.models import MyUser
from shop.models import Product, Comment


postgres_db.connect(reuse_if_open=True)
postgres_db.create_tables([MyUser, Product, Comment])
postgres_db.close()
