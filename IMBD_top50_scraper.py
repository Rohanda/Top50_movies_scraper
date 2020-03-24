from bs4 import BeautifulSoup
import requests

# Ask the user to enter the year used to get top ratings
year = input("Please enter the year you want to get top ratings(e.g: 2016): ")

# Build the url
url = "https://www.imdb.com/search/title/?year="+year+"&title_type=feature&"
Response = requests.get(url)

#Use Beautiful Soup library to find movie titles in the response
Soup = BeautifulSoup(Response.text, 'html.parser')
articles =  Soup.find_all("div",attrs = {"class":"article"})
Main_header = articles[0].h1.string
print(Main_header)
Sub_articles = articles[0].find_all("div",attrs ={"class":"lister-item mode-advanced"})
i = 0
y =[]

# Write all movie titles
for article in Sub_articles :
    y.append({i+1:{"name":article.h3.a.string}})
    print (y[i])
    i = i+1

