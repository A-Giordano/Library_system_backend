# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:39:15 2018

@author: SDis
"""

from Code.Resources_parent_module import Resources


class Books(Resources):
    """Son class of Resources, inherit main data fields, setters and getters from that. Plus, other data and methods."""
    def __init__(self, title, author, publisher, year, ISBN):
        super().__init__(title, author, publisher, year)
        self.damages = "No damages reported"
        self.borrower = None
        # Check ISBN is valid
        if ISBN.isdecimal() and len(ISBN) == 13:
            self.ISBN = ISBN
        else:
            ISBN = input("Please input a valid ISBN Code: ")
            while not (ISBN.isdecimal() and len(ISBN) == 13):
                ISBN = input("Please input a valid ISBN Code: ")
            self.ISBN = ISBN
# Setters
    def set_ISBN(self, ISBN):
        """Method that sets the ISBN code if a proper input was given"""
        if ISBN.isdecimal() and len(ISBN) == 13:
            print("Valid imput, ISBN Sucessfully Changed")
            self.ISBN = ISBN
        else:
            ISBN = input("Please input a valid ISBN Code: ")
            while not (ISBN.isdecimal() and len(ISBN) == 13):
                ISBN = input("Please input a valid ISBN Code: ")
            self.ISBN = ISBN
    def set_damages(self, damage):
        """Method that sets damages of a book object"""
        if self.damages == "No damages reported":
            self.damages = ("-" + damage + "- ")
        else:
            self.damages += ("-" + damage + "- ")
    def set_borrower(self, borrower):
        """Metod that sets the borrower of a book object"""
        self.borrower = borrower
# Getters
    def get_ISBN(self):
        """Metod that returns the ISBN code of a book object"""
        return self.ISBN
    def get_damages(self):
        """Metod that returns damages of a book object"""
        return self.damages
    def get_borrower(self):
        """Method that returns the borrower of a book"""
        return self.borrower
    def get_availability(self):
        """Method that returns True or False whether a book  object is available or not"""
        if self.get_borrower() is None:
            return True
        else:
            return False

    def print_resource_details(self):
        """Method that prints all the details of a book"""
        print(
            f"Book Details:\n{super().get_resource_details()} [Damages:{self.get_damages()}] [ISBN:{self.get_ISBN()}] [Availability:{self.get_availability()}]")

    def print_borrower_details(self):
        print("Borrrower Details:")
        if self.borrower is not None:
            self.borrower.print_personal_details()
        else:
            print("Book not Borrowed")  


