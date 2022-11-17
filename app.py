from flask import Flask, request,render_template
import os

app = Flask(__name__)

picFolder=os.path.join('static','pics')

app.config['UPLOAD_FOLDER'] =picFolder

@app.route("/")
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'],'servicio.jpg')
    return render_template("index.html",user_image=pic1)

if __name__ == "__main__":
    app.run(debug=True,port=8000)