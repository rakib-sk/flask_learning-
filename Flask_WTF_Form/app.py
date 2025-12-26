from flask import Flask, render_template,redirect,url_for,flash
from forms import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sdfjksdhfksdhfkjsdhfkjsdhf'

@app.route("/",methods=["GET","POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        
        if username=="admin" and password=="1234":
            flash("Login successflly","success")
            return redirect(url_for("login"))
            
        else:
            flash("Invalid username or password","danger")
            
    return render_template("login.html",form=form)            
    
if __name__=="__main__":
    app.run(debug=True)