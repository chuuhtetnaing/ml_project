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
	res = requests.get(application_link, headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"})
	soup = BeautifulSoup(res.text, 'html.parser')

	name = soup.find("h1", "AHFaub").text
	
	img_div = soup.find("div", "xSyT2c")
	rating_and_count = soup.find("div", "K9wGie")
	rating = rating_and_count.find("div", "BHMmbe").text
	count = rating_and_count.find("span", "").text
	img = img_div.img["srcset"].split("=")[0]

	
	additional_informations = soup.find_all("div", "hAyfc")
	additional_informations = list(map(additional_informations.__getitem__, [0,1,2,3,4,5,7]))

	information_list = list()
	# ['Updated', 'Size', 'Installs', 'Current Version', 'Requires Android', 'Content Rating', 'In-app Products']

	i = 1
	for additional_information in additional_informations:
		if i == 6:
			content_rating = additional_information.find_all("div")[2].text
			information_list.append(content_rating)
		else:
			other_information = additional_information.find("span", "htlgb").text
			information_list.append(other_information)
		i = i + 1


	result = (rating, count, img, name)

	return render_template("improve.html", results = result, additional_informations = information_list)