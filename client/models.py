from django.db import models

class Client(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.cnpj


class Branch(models.Model):
    cnpj = models.CharField(max_length=14, unique=True)
    name = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False)
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE)

    def __str__(self):
        return self.cnpj