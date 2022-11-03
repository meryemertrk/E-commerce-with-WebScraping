from typing import List

from django.http import HttpResponse
from django.shortcuts import render
from .models import Computer
import mysql.connector
from django.db.models import Q

#anasayfa;
def home(request):
    computers = Computer.objects.all()

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

# CİMRİ KLON BİLGİLERİ;
def cimriHome(request):
    computers = Computer.objects.all()
    query = request.GET.get('q')
    if query:
        computers = computers.filter(
            Q(urunmarka__icontains=query) |
            Q(urunmodel__icontains=query) |
            Q(urunadi__icontains=query)
        ).distinct()

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

#marka filtreleri;
def filteredToHP(request):
    computers = Computer.objects.filter(urunmarka="HP")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToCasper(request):
    computers = Computer.objects.filter(urunmarka="Casper")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)


def filteredToLenovo(request):
    computers = Computer.objects.filter(urunmarka="Lenovo")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToDell(request):
    computers = Computer.objects.filter(urunmarka="Dell")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToMonster(request):
    computers = Computer.objects.filter(urunmarka="Monster")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToHuawei(request):
    computers = Computer.objects.filter(urunmarka="Huawei")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToApple(request):
    computers = Computer.objects.filter(urunmarka="Apple")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToHonor(request):
    computers = Computer.objects.filter(urunmarka="Honor")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToDynabook(request):
    computers = Computer.objects.filter(urunmarka="Dynabook")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

#işlemci tipi filtreleri;
def filteredToAMDRyzen5(request):
    computers = Computer.objects.filter(islemcitipi="AMD Ryzen 5")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToAMDRyzen7(request):
    computers = Computer.objects.filter(islemcitipi="AMD Ryzen 7")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToIntelCoreI5(request):
    computers = Computer.objects.filter(islemcitipi="Intel Core i5")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToIntelCoreI7(request):
    computers = Computer.objects.filter(islemcitipi="Intel Core i7")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToAppleM1(request):
    computers = Computer.objects.filter(islemcitipi="Apple M1")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToIntelCoreI9(request):
    computers = Computer.objects.filter(islemcitipi="Intel Core i9")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

#ram filtreleri;
def filteredTo8GBRAM(request):
    computers = Computer.objects.filter(ram="8 GB")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredTo16GBRAM(request):
    computers = Computer.objects.filter(ram="16 GB")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredTo32GBRAM(request):
    computers = Computer.objects.filter(ram="32 GB")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

#ekran kart filtreleri;
def filteredToDahiliEkranKarti(request):
    computers = Computer.objects.filter(ekrankarti="Dahili Ekran Kartı")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToIntelIrisGraphics(request):
    computers = Computer.objects.filter(ekrankarti="Intel Iris Graphics")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToNvidiaGeForceRTX3060(request):
    computers = Computer.objects.filter(ekrankarti="Nvidia GeForce RTX3060")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToM1Pro14Cekirdekli(request):
    computers = Computer.objects.filter(ekrankarti="M1 Pro 14 Çekirdekli")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToM28Cekirdekli(request):
    computers = Computer.objects.filter(ekrankarti="M2 8 Çekirdekli")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToAMDRadeonGraphics(request):
    computers = Computer.objects.filter(ekrankarti="AMD Radeon Graphics")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToNvidiaGeForceMX450(request):
    computers = Computer.objects.filter(ekrankarti="Nvidia GeForce MX450")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToNvidiaGeForceRTX3080(request):
    computers = Computer.objects.filter(ekrankarti="Nvidia GeForce RTX 3080")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def filteredToIntelUHDGraphics620(request):
    computers = Computer.objects.filter(ekrankarti="Intel UHD Graphics 620")

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

#ürün sıralaması filtreleri;
def ucuzdanPahaliya(request):
    computers = Computer.objects.order_by('trendyolfiyati')

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def pahalidanUcuza(request):
    computers = Computer.objects.order_by('-trendyolfiyati')

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def yuksekPuandanDusukPuana(request):
    computers = Computer.objects.order_by('-puan')

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

def dusukPuandanYuksekPuana(request):
    computers = Computer.objects.order_by('puan')

    context={
        'computers' : computers
    }
    return render(request, "cimriKlon.html", context)

# TRENDYOL KLON BİLGİLERİ;
def trendyolHome(request):
    computers = Computer.objects.all()
    query = request.GET.get('q')
    if query:
        computers = computers.filter(
            Q(urunmarka__icontains=query) |
            Q(urunmodel__icontains=query) |
            Q(urunadi__icontains=query)
        ).distinct()

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

#marka filtreleri;
def filteredToHPTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="HP")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToCasperTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Casper")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)


def filteredToLenovoTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Lenovo")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToDellTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Dell")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToMonsterTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Monster")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToHuaweiTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Huawei")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToAppleTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Apple")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToHonorTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Honor")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToDynabookTRENDYOL(request):
    computers = Computer.objects.filter(urunmarka="Dynabook")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)


#işlemci tipi filtreleri;
def filteredToAMDRyzen5TRENDYOL(request):
    computers = Computer.objects.filter(islemcitipi="AMD Ryzen 5")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToAMDRyzen7TRENDYOL(request):
    computers = Computer.objects.filter(islemcitipi="AMD Ryzen 7")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToIntelCoreI5TRENDYOL(request):
    computers = Computer.objects.filter(islemcitipi="Intel Core i5")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToIntelCoreI7TRENDYOL(request):
    computers = Computer.objects.filter(islemcitipi="Intel Core i7")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToAppleM1TRENDYOL(request):
    computers = Computer.objects.filter(islemcitipi="Apple M1")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToIntelCoreI9TRENDYOL(request):
    computers = Computer.objects.filter(islemcitipi="Intel Core i9")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

#ram filtreleri;
def filteredTo8GBRAMTRENDYOL(request):
    computers = Computer.objects.filter(ram="8 GB")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredTo16GBRAMTRENDYOL(request):
    computers = Computer.objects.filter(ram="16 GB")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredTo32GBRAMTRENDYOL(request):
    computers = Computer.objects.filter(ram="32 GB")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

#ekran kart filtreleri;
def filteredToDahiliEkranKartiTRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="Dahili Ekran Kartı")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToIntelIrisGraphicsTRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="Intel Iris Graphics")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToNvidiaGeForceRTX3060TRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="Nvidia GeForce RTX3060")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToM1Pro14CekirdekliTRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="M1 Pro 14 Çekirdekli")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToM28CekirdekliTRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="M2 8 Çekirdekli")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToAMDRadeonGraphicsTRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="AMD Radeon Graphics")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToNvidiaGeForceMX450TRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="Nvidia GeForce MX450")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToNvidiaGeForceRTX3080TRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="Nvidia GeForce RTX 3080")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def filteredToIntelUHDGraphics620TRENDYOL(request):
    computers = Computer.objects.filter(ekrankarti="Intel UHD Graphics 620")

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

#ürün sıralaması filtreleri;
def ucuzdanPahaliyaTRENDYOL(request):
    computers = Computer.objects.order_by('trendyolfiyati')

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def pahalidanUcuzaTRENDYOL(request):
    computers = Computer.objects.order_by('-trendyolfiyati')

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def yuksekPuandanDusukPuanaTRENDYOL(request):
    computers = Computer.objects.order_by('-puan')

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

def dusukPuandanYuksekPuanaTRENDYOL(request):
    computers = Computer.objects.order_by('puan')

    context={
        'computers' : computers
    }
    return render(request, "trendyolKlon.html", context)

#urun ozellikleri url;
def cimriUrunOzelligi(request,id):
    computers = Computer.objects.filter(id=id)

    context={
        'computers' : computers
    }
    return render(request, "cimriUrunOzelligi.html", context)

def trendyolUrunOzelligi(request,id):
    computers = Computer.objects.filter(id=id)

    context={
        'computers' : computers
    }
    return render(request, "trendyolUrunOzelligi.html", context)

