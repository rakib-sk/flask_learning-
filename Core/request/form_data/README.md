# 🧪 Flask Request Mastery — Form Data (POST) Practice

Flask-এর `request` object হলো user → server এ পাঠানো সব ডেটা পড়ার মূল জায়গা।  
আজকের কাজ فقط **Form Data (POST)**।

---

# 📌 1. Form Data Basics

### ✔ `request.form`
- শুধুই POST form data পড়ে
- `.get()` ব্যবহার করলে key missing হলেও error হয় না

---

# 🎯 Practice Tasks

---

## ✅ Practice Task 1 — `/info`

**Target:**  
- GET → form দেখাবে  
- POST → নাম + ইমেইল রিটার্ন করবে

### ✔ Example Output
```
Hello Rakib! Your email is test@gmail.com
```

### ✔ Code
```python
from flask import Flask, request

app = Flask(__name__)

@app.route("/info", methods=["GET", "POST"])
def info():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Hello {name}! Your email is {email}"

    return '''
    <form method="POST">
        Name: <input type="text" name="name"><br>
        Email: <input type="text" name="email"><br>
        <input type="submit" value="Submit">
    </form>
    '''
```

---

## ✅ Practice Task 2 — `/calc`

**Target:**  
- number1 + number2 → sum রিটার্ন করবে

### ✔ Example Output
```
Sum = 15
```

### ✔ Code
```python
@app.route("/calc", methods=["GET", "POST"])
def calc():
    if request.method == "POST":
        n1 = request.form.get("number1", type=float)
        n2 = request.form.get("number2", type=float)
        return f"Sum = {n1 + n2}"

    return '''
    <form method="POST">
        Number 1: <input type="text" name="number1"><br>
        Number 2: <input type="text" name="number2"><br>
        <input type="submit" value="Calculate">
    </form>
    '''
```

---

## ✅ Practice Task 3 — `/login`

**Target:**  
- username = admin  
- password = 123  
- মিললে success, না মিললে invalid

### ✔ Example Output
```
Login Success
```
অথবা  
```
Invalid Login
```

### ✔ Code
```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            return "Login Success"
        else:
            return "Invalid Login"

    return '''
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
    '''
```

---

# ▶ Run App
```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

# 🎉 Summary

| Route   | Method     | Purpose               |
|---------|------------|----------------------|
| `/info` | GET/POST   | নাম + ইমেইল সংগ্রহ |
| `/calc` | GET/POST   | দুই সংখ্যার যোগফল |
| `/login`| GET/POST   | Simple login check |
