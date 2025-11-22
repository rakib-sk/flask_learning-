from flask import Flask,request

app = Flask(__name__)

@app.route("/login",methods=["GET","POST"])

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" AND password == "admin":
            return "Login succesfully!"
            
        else:
            return "Invalid user name or password!"
    
    return '''
    <form method="POST">
        name: <input type="text" name="username">
        password: <input type="text" name="password">  
        <input type="submit" value="submit">        
    </form>
    
'''    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    