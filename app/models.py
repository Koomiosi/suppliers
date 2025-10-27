from django.db import models

class Supplier(models.Model):
    companyname = models.CharField(max_length=100, default='firma')
    contactname = models.CharField(max_length=100, default='yhteyshenkilo')
    address = models.CharField(max_length=200, default='osoite')
    phone = models.CharField(max_length=20, default='puhelin')
    email = models.EmailField(max_length=100, default='sahkoposti@esimerkki.com')
    country = models.CharField(max_length=50, default='maa')

    def __str__(self):
        return f"{self.companyname} from {self.country}"

class Product(models.Model):
    productname = models.CharField(max_length = 20, default = "laku")
    packagesize = models.CharField(max_length = 20, default = 3)
    unitprice = models.DecimalField(max_digits=8, decimal_places=2, default=1.00)
    unitsinstock = models.IntegerField(default = 3)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.productname} produced by {self.supplier.companyname}"
    
class Customer(models.Model):
    customerfname = models.CharField(max_length=50, default='etunimi')
    customerlname = models.CharField(max_length=50, default='sukunimi')
    address = models.CharField(max_length=200, default='osoite')
    phone = models.CharField(max_length=20, default='puhelin')
    email = models.EmailField(max_length=100, default='sahkoposti@esimerkki.com')
    country = models.CharField(max_length=50, default='maa')