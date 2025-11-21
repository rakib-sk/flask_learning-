from flask import Flask, request, Response, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "super_key"

# Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again!", mimetype="text/plain")

    return '''
        <h1> Login page </h1>
        <form method="POST">
            username: <input type="text" name="username"><br />
            password: <input type="password" name="password"><br />
            <input type="submit" value="Login">
        </form>
    '''

# Welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h1> Welcome {session["user"]} </h1>
            <a href="{url_for("logout")}">Logout</a>
        '''
    return redirect(url_for("login"))

# Logout page
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

# Start server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)