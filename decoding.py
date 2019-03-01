import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/?WT.z_jog=1&hF=t&vS=undefined'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html5lib')

title = soup.find_all('h2', class_='story-heading')
for i in title:
	if i.a:
		print(i.a.text.replace('\n','\t').strip())
	else:
		print(i.contents[0].strip())

# new = [i.text for i in title]
# new = [''.join(i.replace('\n', '\t')) for i in new]
# new = [i.strip() for i in new]

# print (new)