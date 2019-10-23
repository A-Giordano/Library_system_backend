# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:32:40 2018

@author: SDis
"""

class Devices:
    """Class for Devices, containing data fields of each and methods.""" 
    def __init__(self, device_type, brand, model, year, location):
        self.device_type = device_type
        self.brand = brand
        self.model = model
        self.year = year
        self.location = location
        self.availability = bool
        self.repairs_upgrades = "-No repairs or upgrades done on this machine-"
#Setters      
    def set_type_device(self, device_type):
        """Method that sets the type of a device object"""
        self.device_type = device_type
    def set_brand(self, brand):
        """Method that sets the brand of a device object"""
        self.brand = brand
    def set_model(self, model):
        """Method that sets the model of a device object"""
        self.model = model
    def set_year(self, year):
        """Method that sets the year of a device object"""
        self.year = year
    def set_location(self, location):
        """Method that sets the location of a device object"""
        self.location = location
    def set_availability(self, bool):
        """Method that sets the availability of a device object"""
        self.availability = bool
    def set_repair_upgrade(self, repair_upgrade):
        """Method that sets a repir or an upgrade done on a device object"""
        if self.repairs_upgrades == "-No repairs or upgrades done on this machine-":
            self.repairs_upgrades = ("-" + repair_upgrade + "- ")
        else:
            self.repairs_upgrades += ("-" + repair_upgrade + "- ")
#Getters:
    def get_device_type(self):
        """Method that returns the type of a device object"""
        return self.device_type
    def get_brand(self):
        """Method that returns the brand of a device object"""
        return self.brand
    def get_model(self):
        """Method that returns the model of a device object"""
        return self.model
    def get_year(self):
        """Method that returns the year of a device object"""
        return self.year
    def get_location(self):
        """Method that returns the location of a device object"""
        return self.location
    def get_repairs_upgrades(self):
        """Method that returns repairs or upgrades done on a device object"""
        return self.repairs_upgrades
    def get_availability(self):
        """Method that returns Available or Unavailable weather a device object is available or unavailable"""
        if self.check_availability() is False:
            return "Unavailable"
        else:
            return "Available"
        
    def check_availability(self):
        """Method that returns True or False weather a device object is available or unavailable"""
        #if the object is created is supposed to be available even if the availability is not setted
        if self.availability is False:
            return False
        else:
            return True    

    def print_device_details(self):
        """Method that prints all the details of a device object"""
        print(f"Device Details:\n[Type:{self.get_device_type()}] [Brand:{self.get_brand()}] [Model:{self.get_model()}] [Year:{self.get_year()}] [Locatin:{self.get_location()}] [Repairs-Upgrades:{self.get_repairs_upgrades()}] [Availability:{self.get_availability()}]")
        

       
        
        
        
        