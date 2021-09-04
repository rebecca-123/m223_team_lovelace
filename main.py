
from flask import Flask, render_template, request

# create an instance of flask object
app = Flask(__name__)


# home page accessed with http://127.0.0.1:5000/
@app.route("/")
# map URL route for function below
def index():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/ritvik/")
def ritvik():
    return render_template("ritvik.html")


@app.route("/william/")
def william():
    return render_template("william.html")


@app.route("/rebecca/")
def rebecca():
    return render_template("rebecca.html")


@app.route("/christina/")
def christina():
    return render_template("christina.html")


@app.route("/journal/")
def journal():
    return render_template("journal.html")


@app.route('/greetings/', methods=['GET', 'POST'])
def greeting():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("greetings.html", name=name)
    return render_template("greetings.html", name="name")


@app.route("/tpt/")
def tpt():
    return render_template("tpt.html")


if __name__ == "__main__":
    app.run(debug=True)
