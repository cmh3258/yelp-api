from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests

#r = requests.get("http://www.yelp.com/menu/mistral-restaurant-boston/item/grilled-portobello-mushroom-carpaccio")
r = requests.get("http://www.yelp.com/menu/mistral-restaurant-boston/item/seared-foie-gras")
count = 0
'''
for line in r:
	soup = BeautifulSoup(r)
	print soup.body.find('div', attrs={'class':'container'}).text
'''
data = r.text
soup = BeautifulSoup(data)

#for link in soup.find_all('a'):
#	print (link.get('href'))
'''
soup = soup.encode('utf-8').strip("\n")
for line in soup:
	print line

def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')

a= []
b = []
c =[]
d = []
e = []
f = []
a.append(soup.find_all("i", class_="star-img stars_5"))
b.append(soup.find_all("i", class_="star-img stars_4"))
c.append(soup.find_all("i", class_="star-img stars_3"))
d.append(soup.find_all("i", class_="star-img stars_2"))
e.append(soup.find_all("i", class_="star-img stars_1"))
f.append(soup.find_all("i", class_="star-img stars_0"))
'''

##################################
#
#	Getting the ratings for the item
#
##################################
five_star = four_star = three_star = two_star = one_star = null_star = 0
word = soup.find_all("i", class_="star-img stars_5")
for x in word:
	#print word
	five_star += 1


word = soup.find_all("i", class_="star-img stars_4")
for x in word:
	#print word	
	four_star += 1

word = soup.find_all("i", class_="star-img stars_3")
for x in word:
	#print word
	three_star += 1


word = soup.find_all("i", class_="star-img stars_2")
for x in word:
	#print word
	two_star += 1


word = soup.find_all("i", class_="star-img stars_1")
for x in word:
	#print word
	one_star += 1


word = soup.find_all("i", class_="star-img stars_0")
for x in word:
	#print word
	null_star += 1

likes = five_star + four_star + three_star
dislikes = null_star + one_star + two_star
neutral = three_star + two_star

print likes, " : ", neutral, " : ", dislikes

#print word.translate(None, '{,\"<>/')


