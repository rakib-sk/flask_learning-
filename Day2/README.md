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
