# flask_learning-
# All Flask note
# 🚀 Flask Setup Guide (PC & Mobile)

এই ডকুমেন্টে PC (Windows/Linux) এবং Mobile (Termux) – দুই জায়গাতেই Flask সেটআপ করার সম্পূর্ণ গাইড দেয়া হলো।

---

# 📱 1. Flask Setup on Mobile (Termux)

## 🔧 Step 1: Termux Update
```bash
pkg update && pkg upgrade -y
```

## 🔧 Step 2: Python Install
```bash
pkg install python -y
```

## 🔧 Step 3: Flask Install
```bash
pip install flask
```

## 📂 Step 4: Project Structure বানাও
```bash
mkdir flask_app
cd flask_app
mkdir templates
mkdir static
```

## 📝 Step 5: app.py তৈরি করো
```bash
nano app.py
```

**Paste this:**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

## 📝 Step 6: templates/home.html তৈরি করো
```bash
nano templates/home.html
```

**Write:**
```html
<h1>Hello Flask from Mobile!</h1>
```

## 🚀 Step 7: Run Flask
```bash
python app.py
```

🔗 Visit:
```
http://127.0.0.1:5000
```

---

# 💻 2. Flask Setup on PC

# 🟦 A. Windows (using CMD/PowerShell)

## 🧰 Step 1: Python Check
```bash
python --version
```

## 🧰 Step 2: Virtual Environment তৈরি
```bash
python -m venv venv
venv\Scripts\activate
```

## 🧰 Step 3: Flask Install
```bash
pip install flask
```

## 📂 Step 4: Project Structure
```
project/
│── app.py
│── /templates
│     └── home.html
│── /static
```

## 📝 Step 5: app.py লিখো
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
```

## 🚀 Step 6: Run Flask
```bash
python app.py
```
# Day 1  
## First Flask Code  

### 📌 সংক্ষিপ্ত ব্যাখ্যা  
এই কোডটি Flask-এর সবচেয়ে বেসিক (Hello World) প্রজেক্ট।  
এখানে আমরা Flask ইমপোর্ট করেছি, একটি অ্যাপ অবজেক্ট বানিয়েছি,  
একটি route (`/`, `/about`, `/contact`) সেট করেছি, এবং শেষে সার্ভার রান করিয়েছি।  
এটি Flask শেখার প্রথম ধাপ এবং প্রতিটি ওয়েব অ্যাপ এই বেসিক স্ট্রাকচার দিয়ে শুরু হয়।  

---

## 💻 Code  

```python
from flask import Flask  # Import Flask 

app = Flask(__name__)  # Create Flask object

@app.route("/")  # @app is a decorator
def hello():
    return "Hello This is my first Flask app"

@app.route("/about")
def about():
    return "This is about page"

@app.route("/contact")
---

# 🟩 B. Linux / Ubuntu

## Step 1: Install Python
```bash
sudo apt update
sudo apt install python3 python3-pip -y
```

## Step 2: Install Flask
```bash
pip3 install flask
```

Rest is same as Windows setup.

---

# 🎯 Common Problems

### ❗ TemplateNotFound: home.html
➡ তুমি `templates/` ফোল্ডারের বাইরে HTML রেখেছো।  
Fix: সব HTML → templates ফোল্ডারে রাখো।

### ❗ Port already in use
```bash
killall python
```

### ❗ Flask not found
```bash
pip install flask
```

---
# Day 2
## Dynamic web site
- Flask এর সাথে Html link করা
  - Templates folder তৈরি করে তার মধ্য Html রাখতে হবে।
  - flask a render_templates function import করতে হবে।


## make a form
- যে কাজ করতে হবে
  - name - দিতে হবে form এর কারণ name এর সাহায্যে flask form পড়ে।
  - Method - POST হবে যোদি data পড়তে হয়
  - route name html এর action এর সাথে মিল থাকবে।

## JINJA in flask
- এটির সাহায্যে Html এ python varible ar access করা যায়
- {{ varible }}
- example <p> {{ name }} </p>

- condition  লেখা
- example

- isTopper = True
- {% if isTopper %}
    <p> You are a topper </p>
- {% else %}
    <p> You need hard work </p>
- {% endif %}


# Template Inheritance in Flask (Jinja2)

Template Inheritance হলো এমন একটি সিস্টেম যেখানে আপনি আপনার ওয়েবসাইটের সাধারণ layout (header, footer, navbar ইত্যাদি) একবার define করে বাকি সব pages-এ reuse করতে পারেন। এর ফলে কোড clean থাকে, repeat কমে এবং বড় প্রজেক্ট maintain করা সহজ হয়।

---

## 🔥 Template Inheritance কেন দরকার?

- সব পেজে একই ডিজাইন বজায় রাখতে  
- বারবার একই কোড লিখা এড়াতে  
- ছোট template দিয়ে বড় layout বানাতে  
- future update অত্যন্ত সহজ করতে  

---

## 🧩 Template Inheritance কীভাবে কাজ করে?

Jinja2 দুইটি প্রধান ট্যাগ ব্যবহার করে:

- **`{% extends "base.html" %}`** → কোন টেমপ্লেট অন্য layout inherit করছে  
- **`{% block content %}{% endblock %}`** → কোন অংশ override করা হবে

---

## 🧱 Base Template (master layout)

এখানে common header, footer, navbar সব থাকবে।

**`templates/base.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>

    <header>
        <h2>My Website</h2>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
        </nav>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>© 2025 All rights reserved</p>
    </footer>

</body>
</html>
```

---

## 🧾 Child Templates

Child template শুধু base template এর block অংশ override করে।

### `home.html`
```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to Home Page</h1>
<p>This is the main landing page of the website.</p>
{% endblock %}
```

### `about.html`
```html
{% extends "base.html" %}

{% block title %}About Us{% endblock %}

{% block content %}
<h1>About This Project</h1>
<p>This website demonstrates how template inheritance works in Flask.</p>
{% endblock %}
```

---

## 🚀 Flask App Example

**`app.py`**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
```

---

## 🧠 Template Inheritance How It Works (Flow)

1. User `/about` page request করলো  
2. Flask `about.html` render করতে বললো  
3. Template দেখে: "আমি base.html extend করছি"  
4. Jinja2 প্রথমে base.html লোড করে  
5. তারপর about.html এর block content → base layout-এর content জায়গায় বসায়  
6. Final HTML user-এর ব্রাউজারে যায়  

---

## 📁 Recommended Structure

```
project/
│
├── app.py
└── templates/
    ├── base.html
    ├── home.html
    └── about.html
```

---

## ✔️ Summary

- Template inheritance বড় ওয়েব প্রজেক্টে অপরিহার্য  
- Layout একবার লিখলেই সব জায়গায় reuse হয়  
- Update করলে পুরো ওয়েবসাইটে পরিবর্তন দেখা যায়  
- Flask/Jinja2 এই সিস্টেমকে অত্যন্ত simple করেছে  

---

## 🎉 Happy Coding!

# Day 3

## Flask Manual Form Handling  
Form Data কিভাবে manually handle করতে হয় সেটাই আজ শিখবো।  
Flask এর `request` object ব্যবহার করে form থেকে data নেওয়া, validation করা, এবং response পাঠানো এই part-এর মূল কাজ।

---

## 📌 1. Manual Form Handling কী?
- যখন form submit হয়, তখন Flask অটোমেটিক কিছুই করে না।  
- আমাদেরকে নিজের হাতে `request.form` থেকে input নিতে হয়।  
- তারপর manually validation, error message এবং response দিতে হয়।

---

## 📌 2. Basic Form (HTML)
এটা তোমার templates ফোল্ডারের `form.html`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Manual Form Handling</title>
</head>
<body>
    <h2>Contact Form</h2>

    {% if error %}
        <p style="color:red;">{{ error }}</p>
    {% endif %}

    <form method="POST" action="/submit">
        <label>Name:</label>
        <input type="text" name="name"><br><br>

        <label>Message:</label>
        <textarea name="message"></textarea><br><br>

        <button type="submit">Send</button>
    </form>
</body>
</html>
```

---

## 📌 3. Flask App (Manual Handling)

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    msg = request.form.get("message")

    # Validation manually করা হচ্ছে
    if not name or not msg:
        return render_template("form.html", error="All fields are required")

    # Success response
    return f"Thanks {name}! Your message: {msg}"


if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📌 4. Important Concepts (একদম সহজভাবে)

### ✅ `request.form`
- HTML form থেকে data নেওয়ার জায়গা  
- Example:  
  ```python
  name = request.form.get("name")
  ```

### ✅ Validation (Manual)
- কোন field খালি আছে কি না check করার দায়িত্ব developer-এর
  ```python
  if not name:
      error = "Name required"
  ```

### ✅ Redirect vs Render
- ভুল হলে user কে আবার সেই form page-এ পাঠাতে হয়
  ```python
  return render_template("form.html", error="Message required")
  ```

### ✅ POST Method
- Form নিরাপদভাবে পাঠানোর জন্য POST ব্যবহার করা হয়  
- HTML form-এ:  
  ```html
  <form method="POST">
  ```

---

## 📌 5. Common Mistakes (যা অনেকেই ভুল করে)
❌ `method="GET"` রেখে POST data নিতে চাওয়া  
❌ form action ভুল path দেওয়া  
❌ template ফোল্ডারের নাম ভুল লেখা (templates হতে হবে)  
❌ validation না করে সরাসরি data process করা  

---

## 📌 6. Day 3 Practice Tasks

### 🔹 Task 1  
একটি login ফর্ম বানাও যেখানে username এবং password দুইটাই প্রয়োজন হবে।  
Validation:  
- ফাঁকা হলে error  
- সব ঠিক থাকলে “Login Success” দেখাবে

### 🔹 Task 2  
Feedback form বানাও:  
- নাম  
- ইমেইল  
- feedback message  
Validation manually implement করবে।

---

# 📌 1. Flash Message কী?

**Flash Message** = Small one-time message  
যেটা ইউজারকে **পরবর্তী request**-এ দেখানো হয়।

Flask নিজে থেকেই এর জন্য `flash()` এবং `get_flashed_messages()` ফাংশন দেয়।

---

# 📌 2. Flash Message ব্যবহার করতে যা লাগবে
Flask app-এ **secret_key** থাকতে হবে:

```python
from flask import Flask, flash, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = "your_secret_key"
```
## 📌 3. Flash Message সেট করা (Backend)

```python 
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "123":
        flash("Login Successful!", "success")
        return redirect(url_for("home"))
    else:
        flash("Invalid Username or Password", "danger")
        return redirect(url_for("login_page"))
```

## 🔥 এখানে:
- ***"Login Successful!"*** → মেসেজ
- ***"success"*** → ক্যাটাগরি (Bootstrap এর class হিসেবে কাজ করে)
- ***"danger"*** → Error message category


## 📌 4. Template-এ Flash Message দেখানো
***Template-এ সাধারণত base.html এ রাখো:
(Bootstrap alert ব্যবহার করলে সুন্দর দেখাবে)***

```html
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    {% for category, message in messages %}
      <div class="alert alert-{{ category }} mt-2">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
{% endwith %}
```

## 📌 5. Form + Flash Message (Complete Example)
***routes.py***

```python 
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "12345"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")

    if not name:
        flash("Name field cannot be empty!", "warning")
        return redirect(url_for("index"))

    flash(f"Hello {name}, your form submitted successfully!", "success")
    return redirect(url_for("index"))
```


*** index.html***
```html
<!DOCTYPE html>
<html>
<head>
    <title>Flash Message Example</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="p-4">

    <!-- Flash messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, message in messages %}
          <div class="alert alert-{{ category }}">
            {{ message }}
          </div>
        {% endfor %}
      {% endif %}
    {% endwith %}

    <form method="POST" action="/submit">
        <input type="text" name="name" placeholder="Enter your name" class="form-control mb-2">
        <button class="btn btn-primary">Submit</button>
    </form>

</body>
</html>
```

## 📌 7. Common Use Cases

| 📌 Feature        | 🧪 Example                                   |
|-------------------|----------------------------------------------|
| Login success     | `flash("Welcome back!", "success")`          |
| Login error       | `flash("Wrong password!", "danger")`         |
| Form error        | `flash("Please fill all fields!", "warning")`|
| Info message      | `flash("New update available!", "info")`     |


# Flask-WTF Registration Form Project

এই প্রোজেক্টে Flask-WTF ব্যবহার করে একটি সহজ Registration Form তৈরি করা হয়েছে।  
Form validation, flash messages, template inheritance—সবকিছু ক্লিন স্ট্রাকচারে সাজানো হয়েছে।

---

## 📌 Features

- Flask-WTF Form Handling
- CSRF Protection (`form.hidden_tag()`)
- Field Validation (Name, Email, Password)
- Flash Messages (Success Message)
- Template Inheritance (`base.html` → `register.html`)
- Redirect on success (“thank you” page)

---

## 🛠️ Installation & Setup

### 1️⃣ Create virtual environment  
```bash
python -m venv venv
source venv/bin/activate   # Linux / Termux
venv\Scripts\activate      # Windows
```

### 2️⃣ Install dependencies  
```bash
pip install flask flask-wtf
```

---

## 📁 Project Structure

```
project/
│
├── app.py
├── forms.py
├── templates/
│   ├── base.html
│   ├── register.html
│   └── thank.html
└── README.md
```

---

## 📄 forms.py

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegistrationsForm(FlaskForm):
    name = StringField("Full name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField("Register")
```

---

## 📄 app.py

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import RegistrationsForm

app = Flask(__name__) 
app.secret_key = "your_secret_key"

@app.route("/", methods=["GET", "POST"])
def registration():
    form = RegistrationsForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome {name}, you registered successfully!")
        return redirect(url_for("success"))
        
    return render_template("register.html", form=form)
    
    
@app.route("/success")
def success():
    return render_template("thank.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)
```

---

## 📄 templates/base.html

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} Flask-WTF form {% endblock %}</title>
  </head>

  <body>
    <header>
      <h1>Flask WTF Registration</h1>
    </header>

    {% with messages = get_flashed_messages(with_categories=True) %}
      {% if messages %}
        {% for category, msg in messages %}
          <p style="color: green">{{ msg }}</p>
        {% endfor %}
      {% endif %}
    {% endwith %}

    {% block content %}{% endblock %}

    <footer>
      <p>RooTcore6 — All rights reserved</p>
    </footer>
  </body>
</html>
```

---

## 📄 templates/register.html

```html
{% extends "base.html" %}

{% block title %} Register page {% endblock %}

{% block content %}
<h2>Registration Form</h2>

<form method="POST" action="/">
  {{ form.hidden_tag() }}

  <p>
    {{ form.name.label }}<br>
    {{ form.name(size=32) }}<br>
    {% for error in form.name.errors %}
      <span style="color:red;">{{ error }}</span>
    {% endfor %}
  </p>

  <p>
    {{ form.email.label }}<br>
    {{ form.email(size=32) }}<br>
    {% for error in form.email.errors %}
      <span style="color:red;">{{ error }}</span>
    {% endfor %}
  </p>

  <p>
    {{ form.password.label }}<br>
    {{ form.password(size=32) }}<br>
    {% for error in form.password.errors %}
      <span style="color:red;">{{ error }}</span>
    {% endfor %}
  </p>

  <p>{{ form.submit() }}</p>
</form>
{% endblock %}
```

---

## 📄 templates/thank.html

```html
{% extends "base.html" %}

{% block title %} Thank You {% endblock %}

{% block content %}
<h2>Registration Successful!</h2>
<p>Your form was submitted correctly.</p>
{% endblock %}
```

---

## 🚀 Run the App

```bash
python app.py
```

Visit:  
```
http://127.0.0.1:5000/
```

---

## ✔️ Summary

- Form → Validate → Flash → Redirect → Thank Page  
- Flask-WTF + Template Inheritance দিয়ে simple registration system  
- Clean, expandable structure (Login page, DB integration easily add করা যাবে)

---

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
