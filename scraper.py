from bs4 import BeautifulSoup
import requests
import pandas
from datetime import date
from tkinter import *

date = date.today()
url = "https://www.amazon.fr/Logitech-Volant-Course-Cuir-m%C3%A9tal/dp/B00YUIM2J0/?_encoding=UTF8&pd_rd_w=Pu4gD&content-id=amzn1.sym.d01040f0-2953-47b0-8f72-922a5679b397&pf_rd_p=d01040f0-2953-47b0-8f72-922a5679b397&pf_rd_r=03FBKY0FD1VGJXXRF4Q4&pd_rd_wg=1sx4N&pd_rd_r=cb3e0c90-96f1-47b1-a61a-a19f937e4e8f&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0", }

page = requests.get(url, headers=headers)


def scrap():
    if page.ok:
        soup = BeautifulSoup(page.text, 'html.parser')
        prices = soup.find(class_="a-offscreen")
        prix = prices.text

        tableau = {"Date": [date], "Prix": [prix]}
        df = pandas.DataFrame.from_dict(tableau)
        df.to_csv("Prices.csv", mode='a', header=False, index=False)


def refresh():
    window.update()


window = Tk()
window.title("Logitech G29 - Suivi du prix")
window.geometry("500x600")
window.minsize(500, 600)
window.maxsize(500, 600)
window.iconbitmap(
    'C:/Users/sliiz/Documents/Python/price-scraper/Meta-Quest-price-scraper/logo.ico')
window.config(background='#1c1c1c')
titre = Label(window, text="Logitech G29 - Suivi du prix",
              font=("Helvetica", 20), bg="#1c1c1c", fg="WHITE")
titre.pack()
frame = Frame(window, bg="#1c1c1c")
frame.pack()
button = Button(frame, text="Démarrer", bg="#00B8FC",
                fg="#1c1c1c", command=scrap)
button.pack(pady=25)
button = Button(frame, text="Rafraichir", bg="#00B8FC",
                fg="#1c1c1c", command=refresh)
button.pack(pady=40)

window.mainloop()
