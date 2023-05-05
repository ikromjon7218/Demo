from django.db import models

from django.db import models
class Nashriyot(models.Model):
    # Y = [
    #     ("3 yillik", "3 yillik"),
    #     ("4 yillik", "4 yillik"),
    #     ("5 yillik", "5 yillik")
    # ]
    nom = models.CharField(max_length=50, blank=True, verbose_name="Nashriyotning to'liq nomi")
    manzil = models.CharField(max_length=50, blank=True, verbose_name="Manzil")
    # talaba_soni = models.PositiveIntegerField("Umumiy talabalar soni",default=1500)
    # sana = models.DateField(auto_now_add=True)
    # email = models.EmailField(unique=True)
    # yillik = models.CharField(max_length=10, choices=Y, null=True)
    def str(self):
        return f"{self.nom}"

class Kitob(models.Model):
    nom = models.CharField(max_length=50, blank=True, verbose_name="Kitobning to'liq nomi")
    narx = models.CharField(max_length=50, blank=True, verbose_name="Kitobning narxi")
    kelgan_sana = models.DateField(auto_now_add=True)
    nashriyoti =  models.ForeignKey(Nashriyot, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom} ({self.narx})"

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    # rahbar = models.CharField(max_length=20)
    # fan_soni = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.nom} ({self.tel})"

class Sotuv(models.Model):
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
    sana = models.DateField()
    def __str__(self):
        return f"{self.nom}"



#     universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE)itet = models.ForeignKey(Universitet, on_delete=models.CASCADE, verbose_name="Universitet", null="a")