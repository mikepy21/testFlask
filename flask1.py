from flask import jsonify
from flask import Flask
app = Flask(__name__)

l=[]
l.append(1)
l.append('a')
l.append("jsdkjskjhjhluhjkhu")
l.append("6378642376396")
l.append("jsdkjskj")


@app.route("/")
def hello_world():
	resp = jsonify(success=False)
	resp = jsonify(objd=l,success='success',code=200)
	return resp
