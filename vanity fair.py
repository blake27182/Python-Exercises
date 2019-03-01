import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html5lib')

sections = soup.find_all(class_='content-section')
for i in sections:
	pars = (i.find_all('p'))
	for i in pars:
		print(i.text)