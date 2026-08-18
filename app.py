# DBS Prediction - V2

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET",'POST'])
def index():
    return(render_template("index.html")) # trying to retrieve the information from the index.html template

@app.route("/main", methods=["GET",'POST'])
def main():
    return(render_template("main.html")) # trying to retrieve the information from the main.html template

@app.route("/dbs", methods=["GET",'POST'])
def dbs():
    return(render_template("dbs.html")) 

# the following won't be run in the cloud (which is the app)
if __name__ == "__main__":
    app.run()