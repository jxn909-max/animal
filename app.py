from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Duck")
@app.route("/ducksupreme")
def duck():
    return render_template("duck.html")

@app.route("/Chicken")
def chicken():
    return render_template("chickens.html")

@app.route("/Cat")
def cat():
    return render_template("cat.html")

if __name__ == "__main__":
    app.run(port=5678)

