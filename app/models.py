from django.db import models

# Create your models here.
class Muraciet(models.Model):
    ad= models.CharField(verbose_name="Ad", max_length=50)
    soyad= models.CharField(verbose_name="Soyad", max_length=50)
    telefon= models.CharField(verbose_name="Telefon", max_length=50)
    email = models.EmailField(verbose_name="Email")
    qeyd = models.TextField(verbose_name="Qeyd")
class New(models.Model):
    title = models.CharField(verbose_name='Başlıq',max_length=250)
    photo = models.ImageField(verbose_name="Şəkil", upload_to='news/')
    tarix = models.DateField(verbose_name="Tarix",auto_created=True)
    metn = models.TextField("Mətn")

class Product(models.Model):
    name = models.CharField(verbose_name="Ad",max_length=128)
    title= models.CharField(verbose_name="Başlıq",max_length=256)
    cesid = models.CharField(verbose_name="Cesid", max_length=128)
    origin =  models.CharField(verbose_name="Mənşə",max_length=256)
    alcohol = models.FloatField(verbose_name="Spirt")
    manifacture_year = models.IntegerField(verbose_name="Istehsal ili")
    about = models.CharField(verbose_name="Haqqında", max_length=512)
    composition = models.CharField(verbose_name="Tərkibi",max_length=256)
    combination  = models.CharField(verbose_name="Uygunluq",max_length=256)
    temperature  = models.CharField(verbose_name="Temperatur",max_length=256)
    keeping_form  = models.CharField(verbose_name="Saxlama forması",max_length=256)
    photo = models.ImageField(verbose_name="Şəkil", upload_to='products/')

class Map(models.Model):
    name = models.CharField(verbose_name="Ad",max_length=127)
    unvan = models.CharField(verbose_name="Unvan",max_length=255)
    tel1 = models.CharField(verbose_name="Telefon1",max_length=20,blank=True)
    tel2 = models.CharField(verbose_name="Telefon2",max_length=20,blank=True)
    tel3 = models.CharField(verbose_name="Telefon3",max_length=20,blank=True)
    tel4 = models.CharField(verbose_name="Telefon4",max_length=20,blank=True)
    tel5 = models.CharField(verbose_name="Telefon5",max_length=20,blank=True)
    unvanlink = models.CharField(verbose_name="Unvan Linki",max_length=4096)

class HomePage(models.Model):
    field1 = models.CharField(verbose_name="AzAbrau Alt",max_length=255)
    field2= models.CharField(verbose_name="Şəki Şərabı Alt",max_length=255)
    field3 = models.CharField(verbose_name="Haqqımızda Başlıq",max_length=255)
    field4 = models.CharField(verbose_name="Haqqımızda description",max_length=255)

