import requests
from bs4 import BeautifulSoup as bs
import re
#load the page

#r = requests.get("https://keithgalli.github.io/web-scraping/webpage.html")
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

#convert to a beautiful soup object
soup = bs(r.content, 'html.parser')

# print(soup.prettify())

#Navigating using tag names, find and find all

first_header = soup.find("h2")
print(first_header)
print("-------------------------")
#find all

headers = soup.find_all("h2")
# print(headers)

#parsing a list of elements to look for
headers = soup.find_all(['h1', 'h2'])

#you can pass attributes to the find and find all

paragraph = soup.find_all("p", attrs={"id": "paragraph-id"})

#you can nest the find and find all calls
body = soup.find('body')
div = body.find('div')
header = div.find('h1')

# print(header)
# print("-------------------------")
# print(div)
# print("-------------------------")

#we can search for specifiv things in our find / find all calls

string_search = soup.find_all("p", string=re.compile("Some"))
print(string_search)

headers =  soup.find_all("h2", string=re.compile("(H|h)eader"))
print(headers)


#NEXT FUNCTIONALITY .......THE SELECT in beatifulsuop

content = soup.select("p")