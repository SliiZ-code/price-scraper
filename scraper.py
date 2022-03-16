from bs4 import BeautifulSoup
import requests

url="https://www.oculus.com/quest-2/"

page=requests.get(url)

soup=BeautifulSoup(page.text,"html.parser")

prices=soup.find(class_="ckwzve65 i4k41kyg ttdjqg0v oz5golib nd8uflda i7qx9w64 rhjqn6gv p5bjl15m rz0v8pod idg8iwya")
prix=prices.text
print(prix)