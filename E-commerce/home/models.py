from django.db import models

# Create your models here.
class Computer(models.Model):
    n11link = models.CharField(db_column='n11Link', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trendyollink = models.CharField(db_column='trendyolLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hepsiburadalink = models.CharField(db_column='hepsiburadaLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vatanlink = models.CharField(db_column='vatanLink', max_length=255, blank=True, null=True)  # Field name made lowercase.
    urunadi = models.CharField(db_column='urunAdi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    urunmarka = models.CharField(db_column='urunMarka', max_length=255, blank=True, null=True)  # Field name made lowercase.
    urunmodel = models.CharField(db_column='urunModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    n11fiyati = models.CharField(db_column='n11Fiyati', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trendyolfiyati = models.CharField(db_column='trendyolFiyati', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hepsiburadafiyati = models.CharField(db_column='hepsiburadaFiyati', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vatanfiyati = models.CharField(db_column='vatanFiyati', max_length=255, blank=True, null=True)  # Field name made lowercase.
    puan = models.CharField(db_column='puan',max_length=255, blank=True, null=True)
    urunozellikleri = models.TextField(db_column='urunOzellikleri', blank=True, null=True)  # Field name made lowercase.
    n11site = models.CharField(db_column='n11Site', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trendyolsite = models.CharField(db_column='trendyolSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hepsiburadasite = models.CharField(db_column='hepsiburadaSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vatansite = models.CharField(db_column='vatanSite', max_length=255, blank=True, null=True)  # Field name made lowercase.
    islemcitipi = models.CharField(db_column='islemciTipi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ekrankarti = models.CharField(db_column='ekranKarti', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ram = models.CharField(db_column='ram', max_length=255, blank=True, null=True)
    urunfotografilink = models.CharField(db_column='urunFotografiLink', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'computer'

class ComputerforAdmin(models.Model):
    urunadi = models.CharField(db_column='urunAdi', max_length=255, blank=True, null=True)
    urunmarka = models.CharField(db_column='urunMarka', max_length=255, blank=True,null=True)
    urunmodel = models.CharField(db_column='urunModel', max_length=255, blank=True, null=True)  # Field name made lowercase.
    trendyolfiyati = models.CharField(db_column='trendyolFiyati', max_length=255, blank=True, null=True)
    puan = models.CharField(db_column='puan', max_length=255, blank=True, null=True)
    urunozellikleri = models.TextField(db_column='urunOzellikleri', blank=True, null=True)
    islemcitipi = models.CharField(db_column='islemciTipi', max_length=255, blank=True, null=True)
    ekrankarti = models.CharField(db_column='ekranKarti', max_length=255, blank=True,null=True)
    ram = models.CharField(db_column='ram', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'computer'

    def __str__(self):
        return f"{self.urunadi}"
