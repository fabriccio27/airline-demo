from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
        
class Flight(models.Model):
    # por related_name en una instancia de Airport, voy a acceder a inst.departures, 
    # y me va mostrar todos las instancias de Flight que tengan de origin a mi instancia de Airport
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    #en pasajero, hago pasajero.flights y me da todos los vueltos que tiene
    #por otro lado, si hago JFK-HTW.passengers, me da varios pasajeros
    #en un many to many, es como una relacion abierta, vuelo puede tener distintos pasajeros, y pasajeros tomar distintos vuelos
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"