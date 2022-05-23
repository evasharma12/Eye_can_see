from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Relative(models.Model):
    # user = models.ForeignKey(User, on_delete= models.CASCADE, default="1")
    user = models.CharField(max_length=250)
    relation = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to='images/')  


    # def __str__(self) -> str:
    #     return self.relation