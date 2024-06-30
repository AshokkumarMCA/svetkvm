from flask import Flask
from flask import render_template,request,Response
app=Flask(__name__)
app.secret_key="vilkvm"
@app.route('/',methods=["POST","GET"])
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=False)
