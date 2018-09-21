from flask import jsonify
from flask import Flask
app = Flask(__name__)
c=[]
l=[]
l.append(1873184)
l.append('(dob)')
c.append('skjkl')
l.append("=(^)=")
l.append("<'n'>")
l.append("n_n")



@app.route("/")
def hello_world():
	resp = jsonify(success=False)
	resp = jsonify(objd=l,success='success',code=200)
	return resp
