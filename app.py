from flask import Flask
from flask import Flask
from flask import render_template
from flask import request, redirect


app = Flask(__name__)

@app.route("/mypage/me")
def me():
    return render_template('me.html')

@app.route("/mypage/contact")
def contact():
       return render_template('contact.html')

     
