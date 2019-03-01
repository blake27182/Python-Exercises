import requests, io
from bs4 import BeautifulSoup

def getArticle():
	url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html,'html5lib')

	a = []
	b = []
	sections = soup.find_all(class_="content-section")
	for i in sections:
		a = (i.find_all('p'))
		for i in a:
			b.append(i.text)
	b = ' '.join(b)
	b = str(b)
	return b

def save(art):
	with io.open('file.txt', 'w', encoding='utf-8') as openFile:
		openFile.write(art)

if __name__=="__main__":
	article = getArticle()
	save(article)
	print('done')