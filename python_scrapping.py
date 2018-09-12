import bs4
import requests
url= "https://www.google.com/search?q=foss@amrita"
answer=requests.get(url=url)
a=bs4.BeautifulSoup(answer.text,'lxml')
head=a.find_all("h3")
for title in head:
	print(title.get_text())
