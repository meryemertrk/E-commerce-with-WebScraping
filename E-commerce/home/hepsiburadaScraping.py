import mysql.connector
from bs4 import BeautifulSoup
import requests

#hepsiburada webscraping;
def hepsiburadaScraping():
    liste = []
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'})

    URL = "https://www.hepsiburada.com/laptop-notebook-dizustu-bilgisayarlar-c-98"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")

    st1 = soup.find("div", attrs={"class": "productListContent-tEA_8hfkPU5pDSjuFdKG"})
    st2 = st1.find_all("li", attrs={"class": "productListContent-zAP0Y5msy8OHn5z7T_K_"})

    for link in st2:
        bas = "https://www.hepsiburada.com"
        son = link.a.get("href")
        urunLinki = bas + son
        print(urunLinki)

        webpage = requests.get(urunLinki, headers=HEADERS)
        soup1 = BeautifulSoup(webpage.content, "lxml")

        urunAdi = soup1.find("header", attrs={"class": "title-wrapper"}).text.strip()
        stringToList = urunAdi.split()
        urunMarka = stringToList[0]
        urunModel = stringToList[1] + " " + stringToList[2] + " " + stringToList[3]
        print(urunAdi)
        print(urunMarka)
        print(urunModel)

        urunFiyati1 = soup1.find("span", attrs={"data-bind": "markupText:'currentPriceBeforePoint'"}).text.strip()
        urunFiyati2 = soup1.find("span", attrs={"data-bind": "markupText:'currentPriceAfterPoint'"}).text.strip()
        urunFiyati = urunFiyati1 + "," + urunFiyati2 + " TL"
        print(urunFiyati)

        puan = soup1.find("span", attrs={"class": "rating-star"}).text
        print(puan)

        urunOzellikleri = soup1.find("div", attrs={"id": "productTechSpecContainer"}).text.strip().replace("\n", " ")
        print(urunOzellikleri)

        site = "https://images.hepsiburada.net/cac/content/www/erised/globalAssets/images/hepsiburada-logo-1024.png"

        bilgi = {"urunLinki": urunLinki,
                 "urunAdi": urunAdi,
                 "urunMarka": urunMarka,
                 "urunModel": urunModel,
                 "urunFiyati": urunFiyati,
                 "puan": puan,
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
        sql = "INSERT INTO main (urunLinki, urunAdi, urunMarka, urunModel, urunFiyati, puan, urunOzellikleri, site) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (value["urunLinki"], value["urunAdi"], value["urunMarka"], value["urunModel"], value["urunFiyati"], value["puan"], value["urunOzellikleri"], value["site"])
        mycursor.execute(sql, val)
    veritabani.commit()

veri = hepsiburadaScraping()
print(veri)
veritabani = veritabaniBaglantisi()
veriAktarma(veritabani, veri)
