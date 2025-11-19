# flask_learning-
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

# ✅ Conclusion
এই README অনুসরণ করে তুমি PC এবং Mobile—দুই জায়গাতেই ১০০% কার্যকরভাবে Flask রান করতে পারবে। কোনো সমস্যা হলে “error screenshot” পাঠাবে, আমি ঠিক করে দেবো।
