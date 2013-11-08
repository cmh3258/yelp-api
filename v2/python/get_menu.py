from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests

#r = requests.get("http://www.yelp.com/biz/mistral-restaurant-boston#query:mistral%20rset")
r = requests.get("http://www.yelp.com/biz/el-pel%C3%B3n-taquer%C3%ADa-boston-3#query:tacos")
count = 0

data = r.text
soup = BeautifulSoup(data)

try:
	line = soup.find_all("div", class_="yelp-menu")
	for x in line:
		x = x.find("a")
		url = x.get('href')	
		full_url = "http://www.yelp.com"+url
		name = x.getText()
		print full_url, " ", name
		exp = "Explore the Menu"
		name = name.strip(" ")
		print exp, " : ", name
		if name == exp:
			print 'This is a Yelp Menu'
			##########
			#
			#  Will return url 
			#
			##########
		else:
			print 'This is NOT a Yelp menu'
			##########
			#
			#  Will return False
			#
			##########
		

except:
	print 'This is NOT a Yelp menu(x2)'