from flask import Flask, render_template, redirect
app = Flask(__name__)



@app.route('/')

@app.route('/signup')
def home():
  return render_template('sign_up.html')

