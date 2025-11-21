from flask import Flask, request

app = Flask(__name__)

@app.route("/info", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        return f"Hello {username}! Your email is {email}"
    
    return '''
    <form method="POST">
        Name: <input type="text" name="username"><br />
        Email: <input type="text" name="email"><br>
        <input type="submit" value="submit">
    </form>
    '''

if __name__ == "__main__":
    app.run()