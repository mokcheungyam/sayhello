import os
import sys

from sayhello import app

dev_db = "sqlite:///" + os.path.join(os.path.dirname(app.root_path), "data/data.db")
print(dev_db)

SECRET_KEY = os.getenv("SECRET_KEY", "secret string")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", dev_db)

