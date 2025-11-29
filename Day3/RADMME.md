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
