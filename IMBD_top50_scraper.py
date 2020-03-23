from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/search/title/?year=2019&title_type=feature&"
Response = requests.get(url)
Soup = BeautifulSoup(Response.text, 'html.parser')
Re =  Soup.find_all(attrs={"class": "lister-item-index unbold text-primary"})
print(Re[49].next_sibling.next_sibling.string)
#TODO : 1- loop on all titles ,extract them and save them in a json file
#       2-Extract the following info:
#       "1": {
#         "name": "Torpedo Boat, 'Dupont'",
#         "certificate": "",
#         "runtime": "",
#         "genre": "",
#         "description": "\"A stunning view of one of the fastest boats in Uncle Sam's torpedo fleet. She is running under forced draught at full headway, and comes like a race horse directly toward the camera, ...                See full summary\u00a0\u00bb",
#         "director": "",
#         "stars": []
