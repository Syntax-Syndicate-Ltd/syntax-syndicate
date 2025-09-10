import os
from flask import Flask, send_file, render_template 

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/comming-soon")
def comming_soon():
    return render_template("coming-soon.html")

if __name__ == "__main__":
    # Production note: use gunicorn or another WSGI server for public deployments.
    app.run(host="0.0.0.0", port=5000, debug=True)
