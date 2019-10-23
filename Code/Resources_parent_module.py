# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:22:21 2018

@author: SDis
"""
#import Code.Members_module

class Resources:
    """ Parent class for Books and eResources containg the main data fields and related setters and getters"""
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year   
#Setters   
    def set_title (self, title):
        """Method that sets the title of a resource object"""
        self.title = title 
    def set_author (self, author):
        """Method that sets the author of a resource object"""
        self.author = author
    def set_publisher (self, publisher):
        """Method that sets the publisher of a resource object"""
        self.publisher = publisher
    def set_year (self, year):
        """Method that sets the year of a resource object"""
        self.year = year
#Getters  
    def get_title(self):
        """Method that gets the title of a resource object"""
        return self.title
    def get_author(self):
        """Method that gets the author of a resource object"""
        return self.author
    def get_publisher(self):
        """Method that gets the publisher of a resource object"""
        return self.publisher
    def get_year(self):
        """Method that gets the year of a resource object"""
        return self.year

    def get_resource_details (self):
        """Method that returns the main details of a resource object"""
        return (f"[Title:\"{self.get_title()}\"] [Author:{self.get_author()}] [Publisher:{self.get_publisher()}] [Year:{self.get_year()}]")
        

        




