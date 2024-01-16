from django.db import models

# menu and booking models
class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
   inventory = models.SmallIntegerField(default=5)

   def __str__(self):
      return self.title

class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    booking_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=6)

    def __str__(self): 
        return self.first_name



