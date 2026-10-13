# DBS Prediction - V2

from flask import Flask, render_template, request
import joblib
from groq import Groq
import os



client = Groq()

modelPKL = joblib.load("DBS_SingDollar.pkl")

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

@app.route("/chatbot", methods=["GET",'POST'])
def chatbot():
    return(render_template("chatbot.html")) 

@app.route("/DBSresult",methods=["GET",'POST'])
def DBSresult():
    q = float(request.form.get("q"))
    r = modelPKL.predict([[q]])
    return(render_template("DBSresult.html",r=r)) 

@app.route("/chatbotReply",methods=["GET",'POST'])
def chatbotReply():
    q = request.form.get("q")
    r = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": q}
    ]
)

    return(render_template("chatbotReply.html",r=r.choices[0].message.content)) 

# the following won't be run in the cloud (which is the app)
if __name__ == "__main__":
    app.run()