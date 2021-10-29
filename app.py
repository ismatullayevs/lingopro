from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "youwillneverfindthispassword"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        flash("Your request has been sent", "info")
    return render_template("test.html")
