from flask import jsonify
from flask import Flask
app = Flask(__name__)

l=[]
l.append(1873184)
l.append('a')
l.append("jsdk23178371287932jskjhjhluhjkhu")
l.append("83274083274837ac")
l.append("672163723964")


@app.route("/")
def hello_world():
	resp = jsonify(success=False)
	resp = jsonify(objd=l,success='success',code=200)
	return resp
