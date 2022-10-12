from django.db import models

# Create your models here.
class credentials(models.Model):
    address = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    port = models.CharField(max_length=100)

    def __str__(self):
        return self.address, self.database, self.user, self.password, self.port
