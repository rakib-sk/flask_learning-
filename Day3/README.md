
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


# Flash meaasges
## 🌟 Flask Flash Messages — Complete Guide

Flask-এ **Flash Message** ব্যবহার করা হয় ইউজারকে ছোট নোটিফিকেশন দেখানোর জন্য  
যেমন: Login সফল, Error, Warning, Logout, Form validation ইত্যাদি।

এই README-তে তুমি শিখবে:
- Flash কী?
- কীভাবে কাজ করে?
- Backend এ flash সেট করা
- Template এ flash দেখানো
- Message categories (success/error/info/warning)
- Bootstrap দিয়ে সুন্দর alert বানানো

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
