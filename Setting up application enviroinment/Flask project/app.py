from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def flaskproject():
    return """<xmp>
              Team id : PTN2022TMID32153
              Project name : Nutrition assistant application
              Task : Setting up application enviroinment / create flask project
              flask project run successfully
              </xmp>"""