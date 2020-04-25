# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class User(models.Model):
    """
    This model facilitates creating a single login for three types of users.

    -- Roles : Student,Staff,Admin
    __ Attributes: user_id,password,firstName,lastName,phone,email_id,route_id,stop_id
    """
    user_id = models.CharField(max_length=20)
    password= models.CharField(max_length=30)
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email_id = models.CharField(max_length=40)
    route_id = models.CharField(max_length=40)
    stop_id = models.CharField(max_length=10)
    user_role_choices = [("Student","Student"),("Admin","Admin"),("Staff","Staff")]
    user_role = models.CharField(choices=user_role_choices,max_length=30)


class Driver(models.Model):
    """
    Drivers are separated from users since the attributes are different.
    Drivers are only registered/added and never deleted.

    --Attributes
    driver_id,first_name,last_name,joining_date,end_date (Last day of job)

    """
    driver_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    joining_date = models.DateField()
    end_date= models.DateField()


class Bus(models.Model):
    """
    Each bus is treated as an entity with id being its Number-Plate and is assigned to a Route when working.
    This helps to track which bus is assigned to a specific route each day.

    --Attributes
    bus_id,status,capacity
    """
    bus_id= models.CharField(max_length=10)
    status_choice = [("Working","Working"),("Damaged","Damaged"),("Dormant","Dormant")]
    status= models.CharField(choices=status_choice,max_length=30)
    capacity = models.IntegerField()


class Route(models.Model):
    """
    Routes indicate the bus numbers (46,64,12).

    --Attributes
    route_id,type
    """
    route_id = models.CharField(max_length=10)
    type_choice = [("Staff","Staff"),("Student","Student"),("Other","Other")]
    type = models.CharField(choices=type_choice,max_length=30)
    #no_of_stops .. can be calculated ?



