import mysql.connector
from bs4 import BeautifulSoup
import requests

# n11 webscraping;
def n11Scraping():
    liste = []
    r = requests.get("https://www.n11.com/bilgisayar/dizustu-bilgisayar")
    soup = BeautifulSoup(r.content, "lxml")

    st1 = soup.find("div", attrs={"class": "productArea"})
    st2 = st1.find_all("div", attrs={"class": "columnContent"})

    for link in st2:
        urunLinki = link.a.get("href")
        print(urunLinki)

        r1 = requests.get(urunLinki)
        soup1 = BeautifulSoup(r1.content, "lxml")

        urunAdi = soup1.find("h1", attrs={"class": "proName"}).text.strip()
        stringToList = urunAdi.split()
        urunMarka = stringToList[0]
        urunModel = stringToList[1] + " " + stringToList[2] + " " + stringToList[3]
        print(urunAdi)
        print(urunMarka)
        print(urunModel)

        urunAnaFiyat = soup1.find("div", attrs={"class": "unf-p-summary-price"}).text
        urunFiyati = urunAnaFiyat + " TL"
        print(urunFiyati)

        urunOzellikleri = soup1.find("div", attrs={"class": "unf-prop-context"}).text.strip().replace("\n", " ")
        print(urunOzellikleri)

        site = "https://n11scdn.akamaized.net/a1/org/22/06/24/72/96/64/36/96/74/72/45/71/57583492847166994803.svg"

        bilgi = {"urunLinki": urunLinki,
                "urunAdi": urunAdi,
                "urunMarka": urunMarka,
                "urunModel": urunModel,
                "urunFiyati": urunFiyati,
                "urunOzellikleri": urunOzellikleri,
                "site": site}
        liste.append(bilgi)
    return liste

# veritabanı bağlantısı kurulumu;
def veritabaniBaglantisi():
    veritabani=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="proje1"
    )
    return veritabani

# verilerin veritabanına aktarılması;
def veriAktarma(veritabani, veri):
    mycursor = veritabani.cursor()
    for value in veri:
        sql = "INSERT INTO main (urunLinki, urunAdi, urunMarka, urunModel, urunFiyati, urunOzellikleri, site) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (value["urunLinki"], value["urunAdi"], value["urunMarka"], value["urunModel"], value["urunFiyati"], value["urunOzellikleri"], value["site"])
        mycursor.execute(sql, val)
    veritabani.commit()

veri = n11Scraping()
print(veri)
veritabani = veritabaniBaglantisi()
veriAktarma(veritabani, veri)
