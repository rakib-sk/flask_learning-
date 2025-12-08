# Day 5

# 🚀 Flask + SQLAlchemy — Complete Guide (DBMS Connection)

Flask-এ ডাটাবেজ ব্যবহার করতে সবচেয়ে জনপ্রিয় ও সহজ উপায় হলো **SQLAlchemy ORM**।  
এটি তোমাকে Python কোড দিয়েই টেবিল তৈরি, ডাটা ইনসার্ট, আপডেট, ডিলিট এবং কোয়েরি করতে সাহায্য করে — তাই কাঁচা SQL লিখতে হয় না।

এই README.md এ তুমি শিখবে:

- SQLAlchemy কী?
- Flask প্রোজেক্টে কীভাবে সেটআপ করবে
- DBMS (SQLite, MySQL/MariaDB, PostgreSQL) কনফিগারেশন
- Model তৈরি করার নিয়ম
- ডাটাবেজ Create / Insert / Query / Update / Delete
- Project Structure Example

---

## 🔥 SQLAlchemy কী?

SQLAlchemy হলো একটি ORM (Object Relational Mapper) —  
মানে, তুমি Python Class লিখবে আর SQLAlchemy সেই ক্লাসকে ডাটাবেজের টেবিলে রূপান্তর করবে।

যেমন:  
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
```
***এটি অটোমেটিক ডাটাবেজে user নামে টেবিল বানাবে।***


## 📦 Installation
### Termux / PC যেখানেই হও:
```bash
pip install flask flask_sqlalchemy
```
***যদি MySQL/MariaDB ব্যবহার করো:***

```bash
pip install PyMySQL
```

*** PostgreSQL হলে: ***
```bash
pip install psycopg2
```

## 📁 Flask Project Structure
```
project/
│── app.py
│── models.py
│── config.py
│── requirements.txt
└── instance/
     └── dev.db
```

## ⚙️ Step-1: Config Setup (config.py)
```python
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "your-secret-key"

    # SQLite
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance/dev.db")

    # Disable warnings
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

## 🏗️ Step-2: Create Flask App (app.py)
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from models import User
    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        users = User.query.all()
        return {"total_users": len(users)}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
```


## 🧱 Step-3: Create Models (models.py)
```python
from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
```

## 🛠️ Step-4: CRUD Operations
### ✔ Insert Data
```python
new_user = User(name="Rakib", email="rakib@example.com")
db.session.add(new_user)
db.session.commit()
```

### ✔ Read Data
```python
user = User.query.first()
users = User.query.all()
find = User.query.filter_by(name="Rakib").first()
```

### ✔ Update Data
```python
user = User.query.first()
user.name = "Updated Name"
db.session.commit()
```

### ✔ Delete Data
```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

## 🗄️ Using Different DBMS
### 1️⃣ SQLite
***Already used above.***
```
SQLALCHEMY_DATABASE_URI = "sqlite:///instance/dev.db"
```

### 2️⃣ MySQL / MariaDB
***Install Driver:***

```bash
pip install PyMySQL
```

*** Then config: ***
```
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/databasename"
```

***Example***
```
mysql+pymysql://root:1234@127.0.0.1/mydb
```

### 3️⃣ PostgreSQL
```
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost/mydb"
```

## 🧪 Testing the Project
```
python app.py
```

### Then visit:
```
http://127.0.0.1:5000/
```
***যদি {"total_users": 0} দেখায় → DB ঠিকভাবে কনেক্ট হয়েছে।***


## 🎯 Summary

| Task                     | SQLAlchemy Advantage        |
|--------------------------|------------------------------|
| Table Create             | Automatically                |
| CRUD                     | Easy & Clean                 |
| DBMS support             | SQLite, MySQL, PostgreSQL    |
| Python Class → Table     | Auto mapping                 |
| Safe Queries             | Injection protected          |


## 👍 Conclusion
Flask + SQLAlchemy হলো সবচেয়ে ক্লিন ও প্রোডাকশন-রেডি ডাটাবেজ সলিউশন।
ORM ব্যবহার করলে ভবিষ্যতে প্রোজেক্ট বড় হলেও কোড সুন্দর ও পরিচালনা সহজ থাকে।
