# from bs4 import BeautifulSoup

import requests
from flask import Flask, session, render_template, redirect, url_for, request


price = requests.get("https://data.fixer.io/api/convert?access_key=49877dc2261a4302464cfb957fac4e97&from=MYR&to=USD&amount=25").json()['result']

print(price)
# res = requests.get("https://play.google.com/store/apps/details?id=com.mojang.minecraftpe", headers={"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1"})
# soup = BeautifulSoup(res.text, 'html.parser')
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





# additional_informations = soup.find_all("div", "hAyfc")
# additional_informations = list(map(additional_informations.__getitem__, [0,1,2,3,4,5,7]))

# information_list = list()
# ['Updated', 'Size', 'Installs', 'Current Version', 'Requires Android', 'Content Rating', 'In-app Products']
# print(additional_informations)

# <h5>Updated: {{additional_informations[0]}}</h5>
# <h5>Size: {{additional_informations[1]}}</h5>
# <h5>Installs: {{additional_informations[2]}}</h5>
# <h5>Current Version: {{additional_informations[3]}}</h5>
# <h5>Requires Android: {{additional_informations[4]}}</h5>
# <h5>Content Rating: {{additional_informations[5]}}</h5>
# <h5>In-app Products: {{additional_informations[6]}}</h5>
# <h5>Category: {{additional_informations[7]}}</h5>

# print(additional_informations)

# if additional_informations[0].find("span", "htlgb").text == 'Learn More':
# 	information_list.append(additional_informations[1].find("span", "htlgb").text)
# 	information_list.append(additional_informations[2].find("span", "htlgb").text)
# 	information_list.append(additional_informations[3].find("span", "htlgb").text)
# 	information_list.append(additional_informations[4].find("span", "htlgb").text)
# 	information_list.append(additional_informations[5].find("span", "htlgb").text)
# 	additional_informations = soup.find_all("div", "hAyfc")
# 	additional_informations = list(map(additional_informations.__getitem__, [6]))
# 	information_list.append(additional_informations[0].find("span", "htlgb").text)
# 	additional_informations = soup.find_all("div", "hAyfc")
# 	additional_informations = list(map(additional_informations.__getitem__, [8]))
# 	information_list.append((additional_informations[0].find("span", "htlgb").text).replace(u'\xa0', u' '))
	
	# information_list.append(additional_informations[7].find("span", "htlgb").text)

# print(information_list)
# additional_informations = soup.find_all("div", "hAyfc")
# additional_informations = list(map(additional_informations.__getitem__, [8]))
# print(additional_informations)
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
# 	else:
# 		other_information = additional_information.find("span", "htlgb").text
# 		information_list.append(other_information)
# 	i = i + 1

# https://play.google.com/store/apps/details?id=com.craftgames.worldcrft
# ['November 13, 2019', '80M', '10,000,000+', '3.4.11', '4.1 and up', 'Rated for 3+', 'RM\xa03.84 - RM\xa0207.69 per item']
# ['November 12, 2019', 'Varies with device', '10,000,000+', '1.13.1.5', '4.2 and up', 'Rated for 7+Fear, Mild ViolenceLearn More']
# ['November 12, 2019', 'Varies with device', '10,000,000+', '1.13.1.5', '4.2 and up', 'Rated for 7+Fear, Mild ViolenceLearn More', 'RM 1.46 - RM 209.99 per item']


# print(information_list)