# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
