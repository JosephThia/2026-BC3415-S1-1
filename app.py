# DBS Prediction - V2

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET",'POST'])
def index():
    return('hi')

# the following won't be run in the cloud (which is the app)
if __name__ == "__main__":
    app.run()