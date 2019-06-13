from bs4 import BeautifulSoup
import requests
import lxml
page = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").text
soup= BeautifulSoup(page,'lxml')
with open('article.txt', 'a') as f:    
    for tag in soup.find_all("section"):       
        try:   
            f.write(tag.p.text)
        except:
            pass

print("DONE")


