#!/usr/bin/python3
"""
    Sript that starts a Flask web application
 """
from flask import Flask, render_template, request, abort
import json
import subprocess
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
	#get contributors

	return(render_template("auth.html", repos=result))

def OAUTH(user, pw):
	url = "https://api.github.com/user/repos"
	x = subprocess.check_output(["curl", "-u", "{}:{}".format(user,pw), url]).decode("utf-8")

	return(json.loads(x))

if __name__ == '__main__':
        app.run(port=5007, threaded=True)