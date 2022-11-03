import mysql.connector

def duplicateIslemi():
    try:
        baglanti = mysql.connector.connect(host='localhost',
                                        database='proje1',
                                        user='root')
        cursor = baglanti.cursor()

        # yeni kayıt eklendiğinde tekrar edilen kaydın silinmesi (delete duplicate)
        sql_delete_duplicate = """DELETE urun1 from computer urun1
                                INNER JOIN computer urun2
                                WHERE urun1.id > urun2.id AND urun1.urunModel = urun2.urunModel"""

        cursor.execute(sql_delete_duplicate)
        baglanti.commit()
        print('Silinen sutün sayısı: ', cursor.rowcount)

    except mysql.connector.Error as error:
        print("Veri silinemedi: {}".format(error))

    finally:
        if baglanti.is_connected():
            cursor.close()
            baglanti.close()
            print("MySQL bağlantısı kapatıldı.")

duplicateIslemi()
