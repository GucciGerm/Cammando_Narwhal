#!/usr/bin/python3
"""

"""
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import json
import subprocess

########################################
# Phase 1, initialize datetime commit dictionary

def init_bookkeeping():
	book_keepings = {}
	current_date = datetime.now()
	first_date = current_date - relativedelta(years=1)
	counter = first_date
	while counter <= current_date:
		book_keepings[counter.strftime("%Y-%m-%d")] = 0
		counter = counter + timedelta(days=1)
	return book_keepings

########################################
# Phase 2, count all commits for that year

def populate_bookkeeping(book_keepings, user, pw):
	## loop through all repos
	url = "https://api.github.com/user/repos"
	x = subprocess.check_output(["curl", "-u", "{}:{}".format(user,pw), url]).decode("utf-8")
	#loop through all commits
	repos = json.loads(x)
	last_year = book_keepings.keys();
	for repo in repos:
		print(type(repo))
		commits_url = "https://api.github.com/repos/{}/{}/commits".format(user, repo.get('name'))
		z = subprocess.check_output(["curl", "-u", "{}:{}".format(user,pw), commits_url]).decode("utf-8")
		commits = json.loads(z)
		for commi in commits:
			if type(commi) == str:
				continue
			print(type(commi))
			print(commi)
			commit_dict = commi.get("commit")
			print(type(commit_dict))
			author_dict = commit_dict.get("author")
			date_string = author_dict.get("date")
			commit_date = datetime.strptime(date_string,"%Y-%m-%dT%H:%M:%SZ")
			if commit_date in last_year:
				book_keepings[commit_date] += 1
			else:
				print(commit_date)

if __name__ == '__main__':
	user = "GucciGerm"
	pw = "Gokutheshiba1"
	book_keepings = init_bookkeeping()
	populate_bookkeeping(book_keepings, user, pw)
	print(book_keepings.values())