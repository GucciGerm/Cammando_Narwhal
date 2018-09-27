#!/usr/bin/python3
"""
    Sript that starts a Flask web application
 """
from flask import Flask, render_template, request, abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_narwhal():
    """
        function to return Hello narwhal!
    """
    return render_template("home.html")

@app.route('/authenticate', strict_slashes=False, methods=['POST'])
def authenticate():
	"""

	"""
	req_json = request.form
	if req_json.get("username") is None:
		abort(400, "Missing username")
	if req_json.get("password") is None:
		abort(400, "Missing password")
	username = req_json.get("username")
	password = req_json.get("password")

	result = OAUTH(username, password)

	return(render_template("auth.html", username=username, password=password))

def OAUTH(user, pw):
	pass

if __name__ == '__main__':
        app.run(port=5007, threaded=True)