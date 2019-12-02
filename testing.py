from bs4 import BeautifulSoup

import requests
from flask import Flask, session, render_template, redirect, url_for, request


res = requests.get("https://play.google.com/store/apps/details?id=com.google.android.youtube", headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"})
soup = BeautifulSoup(res.text, 'html.parser')
# additional_information = soup.find_all("span", "htlgb")

# for aa in additional_information:
# 	if aa.find("span", "htlgb"):
# 		print(aa.find("span", "htlgb").text)

# aa = additional_information.find_all("div", "IQ1z0d")
# for aa in additional_information:
	# print(aa.prettify())


# additional_information = soup.find_all("div", "hAyfc")
# additional_information = list(map(additional_information.__getitem__, [0,1,2,3,4,5,7]))

# information_list = list()
# # ['Updated', 'Size', 'Installs', 'Current Version', 'Requires Android', 'Content Rating', 'In-app Products']

# i = 1
# for t in additional_information:
# 	if i == 6:
# 		aaa = t.find_all("div")[2].text
# 		print(aaa)
# 	else:
# 		a = t.find("span", "htlgb").text
# 		print(a)

# 	i = i + 1



category = soup.find_all("a", "hrTbp R8zArc")[1]['href']
category = category.split("/")[-1]

print(category)


# additional_informations = list(map(additional_informations.__getitem__, [0,1,2,3,4,5,7]))

# information_list = list()
# # ['Updated', 'Size', 'Installs', 'Current Version', 'Requires Android', 'Content Rating', 'In-app Products']

# i = 1
# for additional_information in additional_informations:
# 	if i == 6:
# 		check_content = additional_information.find("div", "BgcNfc").text
# 		if check_content != "Content Rating":
# 			information_list.append("No content rating is available")
# 		else:
# 			content_rating = additional_information.find_all("div")[2].text
# 			information_list.append(content_rating)
# 	elif i == 7:
# 		check_content = additional_information.find("div", "BgcNfc").text
# 		if check_content != "In-app Products":
# 			information_list.append("No in-app purchase is shown")
# 		else:
# 			in_app_purchase = additional_information.find("span", "htlgb").text
# 			information_list.append(in_app_purchase)

# 		# print(additional_information)
# 	else:
# 		other_information = additional_information.find("span", "htlgb").text
# 		information_list.append(other_information)
# 	i = i + 1


# print(information_list)



# for t in additional_information:
# 	aa = t.find_all("span", "htlgb")
# 	bb = aa.find_all("div")
# 	for a in aa:
# 		print(a)






