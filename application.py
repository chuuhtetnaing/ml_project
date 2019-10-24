import os

from flask import Flask, session, render_template, redirect, url_for, request
from bs4 import BeautifulSoup

import requests
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
	
	return render_template("index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
	application_name = request.form.get("application_name")
	print("######")
	print(application_name)
	print("######")
	res = requests.get(f"https://play.google.com/store/search?q={application_name}&c=apps")

	soup = BeautifulSoup(res.text, 'html.parser')

	applications = soup.find_all("div", "ImZGtf mpg5gc")

	img_list = list()
	title_list = list()
	link_list = list()
	results = list()

	for application in applications:
		title = application.find("div", "WsMG1c nnK0zc").text
		image = application.img['data-srcset'].split("=")[0]
		link = "https://play.google.com" + application.a['href']
		img_list.append(image)
		title_list.append(title)
		link_list.append(link)

	results = list(zip(img_list,title_list,link_list))
	
	return render_template("search.html", results = results)

@app.route("/improve", methods=["GET", "POST"])
def improve():
	application_link = request.form.get("application_link")
	res = requests.get(application_link)

	soup = BeautifulSoup(res.text, 'html.parser')
	rating = soup.find("div", "K9wGie")
	result = rating

	return render_template("improve.html", results = result)