import mysql.connector
from bs4 import BeautifulSoup
import requests

# vatan webscraping;
def vatanScraping():
    liste = []
    r = requests.get("https://www.vatanbilgisayar.com/notebook")
    soup = BeautifulSoup(r.content, "lxml")

    st1 = soup.find("div", attrs={"class": "wrapper-product wrapper-product--list-page clearfix"})
    st2 = st1.find_all("div", attrs={"class": "product-list product-list--list-page"})

    for link in st2:
        bas = "https://www.vatanbilgisayar.com"
        son = link.a.get("href")
        urunLinki = bas + son
        print(urunLinki)

        r1 = requests.get(urunLinki)
        soup1 = BeautifulSoup(r1.content, "lxml")

        urunAdi = soup1.find("h1", attrs={"class": "product-list__product-name"}).text.strip()
        stringToList = urunAdi.split()
        urunMarka = stringToList[0]
        urunModel = stringToList[1] + " " + stringToList[2] + " " + stringToList[3]
        print(urunAdi)
        print(urunMarka)
        print(urunModel)

        urunFiyatMiktari = soup1.find("span", attrs={"class": "product-list__price"}).text
        urunFiyatBirimi = soup1.find("span", attrs={"class": "product-list__currency"}).text
        urunFiyati = urunFiyatMiktari + (" ") + urunFiyatBirimi
        print(urunFiyati)

        puan = soup1.find("strong", attrs={"id": "averageRankNum"}).text
        print(puan)

        urunOzellikleri = soup1.find("div", attrs={"id": "urun-ozellikleri"}).text.strip().replace("\n", " ")
        print(urunOzellikleri)

        site = "https://eu001.leafletscdns.com/com.tr/data/9/logo.png"

        bilgi = {"urunLinki":urunLinki,
                "urunAdi":urunAdi,
                "urunMarka":urunMarka,
                "urunModel":urunModel,
                "urunFiyati":urunFiyati,
                "puan":puan,
                "urunOzellikleri":urunOzellikleri,
                "site":site}
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
        sql = "INSERT INTO main (urunLinki, urunAdi, urunMarka, urunModel, urunFiyati, puan, urunOzellikleri, site) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (value["urunLinki"], value["urunAdi"], value["urunMarka"], value["urunModel"], value["urunFiyati"], value["puan"], value["urunOzellikleri"], value["site"])
        mycursor.execute(sql, val)
    veritabani.commit()

veri = vatanScraping()
print(veri)
veritabani = veritabaniBaglantisi()
veriAktarma(veritabani, veri)




