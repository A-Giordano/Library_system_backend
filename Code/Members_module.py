# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:23:10 2018

@author: SDis
"""
#import Code.system

from Code.Books_module import Books



class Members:
    """Class for members of the Library containing data field of each and methods""" 
    def __init__(self, name, surname, date_of_birth, residence):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.residence = residence
        self.notifications = None 
        self.borrowed_books = []
#Setters
    def set_name(self, name):
        """Method that sets name of a member object"""
        self.name = name
    def set_surname(self, surname):
        """Method that sets surname of a member object"""
        self.surname = surname
    def set_date_of_birth(self, date_of_birth):
        """Method that sets date of birth of a member object"""
        self.date_of_birth = date_of_birth
    def set_residence(self, residence):
        """Method that sets residence of a member object"""
        self.residence = residence
    def set_notification(self, notification):
        """Method that sets a notification to a member object"""
        if self.notifications == None:
            self.notifications = ("-" + notification + "- ")
        else:
            self.notifications += ("-" + notification + "- ")
#Getters
    def get_name(self):
        """Method that returns name of a member object"""
        return self.name
    def get_surname(self):
        """Method that returns surname of a member object"""
        return self.surname
    def get_date_of_birth(self):
        """Method that returns date of birth of a member object"""
        return self.date_of_birth
    def get_residence(self):
        """Method that returns residence of a member object"""
        return self.residence      
    def get_borrowed_books(self):
        """Method that returns a list of the borrowed book by a member object"""
        return self.borrowed_books  
    def get_notifications(self):
        """Method that returns notifications of a member object"""
        return self.notifications
    def get_borrowed_books_lengh(self):
        """Method that returns number of books borrowed by a member object"""
        return (len(self.borrowed_books))

    def add_book(self, book):
        """Method that adds a book to the list of borrowed books by a member object"""
        self.borrowed_books.append(book)
 
    def print_personal_details(self):
        """Method that prints all the personal details of a member object"""
        print(f"Member Personal Details:\n[Name:{self.get_name()}] [Surname:{self.get_surname()}] [Date of birth:{self.get_date_of_birth()}] [Residence:{self.get_residence()}]")

    def print_notifictaions(self):
        """Method that prints all the notifications of a member object"""
        print(f"!! {self.get_name()} {self.get_surname()}, here your Notifinations:{self.get_notifications()} !!")

    def print_borrowed_books_details(self):
        """Method that prints all the details of all books borrowed by a member object"""
        for book in self.borrowed_books:              
            print(f"You are currently borowing {self.get_borrowed_books_lengh()} item/s:")
            book.print_resource_details()
       








