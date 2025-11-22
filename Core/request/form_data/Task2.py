from flask import Flask,request

app = Flask(__name__)

@app.route("/calc",methods=["GET","POST"])
def sum():
    if request.method == "POST":
        num1 = int(request.form.get("numbar1"))
        num2 = int(request.form.get("numbar2"))
        Sum = num1 + num2
        return f"Sum is {Sum}"
    return '''
    <form method = "POST">
        numbar1: <input type="numbar" name="numbar1"><br>
        numbar2: <input type="numbar" name="numbar2">
        <input type="submit" value="submit">
    </form>
'''    

if __name__ == "__main__":
    app.run()
