from bs4 import BeautifulSoup
import requests
import mysql.connector

# trendyol webscraping;
def trendyolScraping():
        liste = []
        r = requests.get("https://www.trendyol.com/laptop-x-c103108")
        soup = BeautifulSoup(r.content, "lxml")

        st1 = soup.find("div", attrs={"class": "prdct-cntnr-wrppr"})
        st2 = st1.find_all("div", attrs={"class": "p-card-wrppr with-campaign-view"})

        for link in st2:
            bas = "https://www.trendyol.com"
            son = link.a.get("href")
            urunLinki = bas + son
            print(urunLinki)

            r1 = requests.get(urunLinki)
            soup1 = BeautifulSoup(r1.content, "lxml")

            urunMarkasi = soup1.find("h1", attrs={"class": "pr-new-br"})
            urunMarka = urunMarkasi.select_one(":nth-child(1)").text
            print(urunMarka)

            urunAdi = soup1.find("h1", attrs={"class": "pr-new-br"}).text.strip()
            print(urunAdi)

            stringToList = urunAdi.split()
            urunModel = stringToList[1] + " " + stringToList[2] + " " + stringToList[3]
            print(urunModel)

            urunFiyati = soup1.find("span", attrs={"class": "prc-dsc"}).text
            print(urunFiyati)

            urunOzellikleri = soup1.find("ul", attrs={"class": "detail-attr-container"}).text.strip()
            print(urunOzellikleri)

            site = "https://cdn.dsmcdn.com/web/logo/ty-web.svg"

            genelUrunOzellikleri = soup1.find("div", attrs={"class": "starred-attributes"})
            islemciTipiFull = genelUrunOzellikleri.select_one(":nth-child(1)")
            islemciTipi = islemciTipiFull.select_one(":nth-child(3)").text
            print(islemciTipi)

            ekranKartiFull = genelUrunOzellikleri.select_one(":nth-child(4)")
            ekranKarti = ekranKartiFull.select_one(":nth-child(3)").text
            print(ekranKarti)

            ramFull = genelUrunOzellikleri.select_one(":nth-child(5)")
            ram = ramFull.select_one(":nth-child(3)").text
            print(ram)

            urunFotografiFull = soup1.find("div", attrs={"class": "gallery-container"})
            urunFotografiLink = urunFotografiFull.img.get("src")
            print(urunFotografiLink)

            bilgi = {"urunLinki": urunLinki,
                     "urunAdi": urunAdi,
                     "urunMarka": urunMarka,
                     "urunModel": urunModel,
                     "urunFiyati": urunFiyati,
                     "urunOzellikleri": urunOzellikleri,
                     "site": site,
                     "islemciTipi": islemciTipi,
                     "ekranKarti": ekranKarti,
                     "ram": ram,
                     "urunFotografiLink": urunFotografiLink}
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
        sql = "INSERT INTO main (urunLinki, urunAdi, urunMarka, urunModel, urunFiyati, urunOzellikleri, site, islemciTipi, ekranKarti, ram, urunFotografiLink) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (value["urunLinki"], value["urunAdi"], value["urunMarka"], value["urunModel"], value["urunFiyati"], value["urunOzellikleri"], value["site"], value["islemciTipi"], value["ekranKarti"], value["ram"], value["urunFotografiLink"])
        mycursor.execute(sql, val)
    veritabani.commit()

veri = trendyolScraping()
print(veri)
veritabani = veritabaniBaglantisi()
veriAktarma(veritabani, veri)
