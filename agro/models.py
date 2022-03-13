from re import M
from sqlite3 import Time
from django.db import models
from numpy import vander


class TimedBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class User(TimedBaseModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(verbose_name="User id", unique=True, default=1)
    name = models.CharField(verbose_name="Name", max_length=100)


    def __str__(self):
        return f"№{self.id} ({self.user_id}) - {self.name}"


    
class Questions(TimedBaseModel):
    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    id = models.AutoField(primary_key=True)

    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    images = models.TextField(verbose_name="All images", null=True, blank=True)
    question = models.TextField(verbose_name="Question")



class Zonts(TimedBaseModel):
    class Meta:
        verbose_name = "Zont"
        verbose_name_plural = "Zonts"


    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    zont_id = models.BigIntegerField(verbose_name="Zont id",null=True, blank=True)
    location = models.URLField(verbose_name="Location")


class ZontImages(TimedBaseModel):
    class Meta:
        verbose_name = "Zont image"
        verbose_name_plural = "Zonts Images"
    
    zont_id = models.BigIntegerField(verbose_name="Zont id",null=True, blank=True)
    images = models.TextField(verbose_name="Images list")


class Problems(TimedBaseModel):

    class Meta:
        verbose_name = "Problem"
        verbose_name_plural = "Problems"

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    image = models.CharField(verbose_name="Image", max_length=255)
    where = models.CharField(max_length=255, verbose_name="Where illness")
    type_illness = models.CharField(max_length=255, verbose_name="Type illness")
    



