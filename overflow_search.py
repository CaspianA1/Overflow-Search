# overflow_search.py

import requests

from bs4 import BeautifulSoup

import os

os.system(["clear", "cls"][os.name == "nt"])

print("OVERFLOW SEARCH ENGINE\t\t\t\n")

help_needed = input("What do you need help with? \x1b[5m->\x1b[25m ")

page = requests.get(f"https://stackoverflow.com/search?q={help_needed}")
# print(f"Your page is: https://stackoverflow.com/search?q={help_needed}")
soup = BeautifulSoup(page.content, "html.parser")


link_list = []
for link in soup.find_all("a",{"class": "question-hyperlink"}): 
	# print(link.get('href'))
	link_list.append(link.get('href'))

print("\nThese links should help you with your problem:\n ")
print(f"\thttps://stackoverflow.com/{link_list[0]}")
print(f"\thttps://stackoverflow.com/{link_list[1]}")
print(f"\thttps://stackoverflow.com/{link_list[2]}\n")