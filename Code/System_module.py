# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:21:56 2018

@author: SDis
"""

from Code.Books_module import Books
from Code.E_Resources_module import E_Resources
from Code.Members_module import Members

class System:
    """Class for the actual System of the Library containing data field of it and methods to run the library""" 
    def __init__(self):
        self.library_name = "default"
        self.address = "default"
        self.catalogue = []
        self.borrower_list = []        
#Setters
    def set_library_name(self, library_name):
        """Method that sets name of a library sistem object"""
        self.library_name = library_name
    def set_address(self, address):
        """Method that sets address of a library sistem object"""
        self.address = address       
#Getters    
    def get_library_name(self):
        """Method that returns name of a library sistem object"""
        return self.library_name
    def get_address(self):
        """Method that returns address of a library sistem object"""
        return self.address
    def get_catalogue(self):
        """Method that returns the catalogue of a library sistem object"""
        return self.catalogue
    def get_catalogue_lengh(self):
        """Method that return the number of resources in the catalogue"""
        return (len(self.catalogue))
    
    def check_resource(self, resource):
        """Method that cheeck if a resource is actually in the catalogue"""
        if resource in self.catalogue:
            return True
        else:
            return False
        
    def edit_resource(self, resource, title):
        """Method that allow to edit the title of a resource object"""
        if self.check_resource(resource) is True:
            resource.set_title(title)
        else:
            print(f"\"{resource.get_title()}\" not contained in the catalogue")
            
    def search_resource(self, resource):
        """Method that search and return a resource object if it is actually in the catalogue"""
        if resource in self.catalogue:
            return resource
        return None
    
    def search_by_ISBN(self, ISBN):
        """Method that search by ISBN and return details of all the objects with that ISBN"""
        n_of_resources = 0            
        for  resource in self.catalogue:
            try:
                if resource.ISBN is ISBN:
                    n_of_resources += 1
                    resource.print_resource_details()
########just for testing pourposes (doesn't affect final user, but meant to be removed):####
                    return 1
############################################################################################
            except AttributeError:
                continue
        if n_of_resources is 0:
            print(f"ISBN code:{ISBN} not contained in the catalogue")
########just for testing pourposes (doesn't affect final user, but meant to be removed):####
            return 0
############################################################################################
        else:
            print(f"Total amount of Resources with \"{ISBN}\" ISBN code: {n_of_resources}\n")
            
    def search_by_author(self, author):
        """Method that search by author and return details of all the objects with that author"""
        n_of_resources = 0
        for resource in self.catalogue:
            if resource.author is author:
                n_of_resources += 1
                resource.print_resource_details()
########just for testing pourposes (doesn't affect final user, but meant to be removed):####
                return 1
############################################################################################
        if n_of_resources is 0:
            print(f"Author:\"{author}\" not contained in the catalogue")
########just for testing pourposes (doesn't affect final user, but meant to be removed):####
            return 0
############################################################################################
        else:
            print(f"Total amount of resource from \"{author}\": {n_of_resources}")
 
    def remove_resource(self, resource):
        """Method that remove a resource based from the object resource itself from the catalogue"""
        if resource in self.catalogue:
            self.catalogue.remove(resource)
        else:
            print(f"Resource \"{resource.get_title()}\" not in the catalogue")
            
    def delete_resource_from_index_position(self, index_position):
        """Method that remove a resource based on index position from the catalogue"""
        if int(index_position) <= (self.get_catalogue_lengh() - 1) and int(index_position) >= 0 :
            del(self.catalogue[index_position])
        else:
            print(f"\"{index_position}\" Index Position not in the catalogue")
            
    def prinit_all_available_books_datails(self):
        """Method that print deatails for all available books"""
        print("Books currently available:")
        for book in self.catalogue:
            if isinstance(book, Books) and book.get_borrower() is None:
                book.print_resource_details()
                
    def add_resource(self, resource):
        """Method that add a resource to the catalogue"""
        if resource in self.catalogue:
            print(f"\"{resource.get_title()}\" is already in the catalogue")
        else:
            self.catalogue.append(resource)
            
    def lending_process(self, book, member):
        """Method that simulate the process of lending a book"""
        if member.get_borrowed_books_lengh() < 5:
            if isinstance(book, Books):
                if self.check_resource(book) is True:   
                    if book.get_availability() is True:
                        book.set_borrower(member)
                        member.borrowed_books.append(book)                             
                    else:
                        print("The book is currently borrowed by another member of the Library")                      
                else:
                    print("The resouurce you are trying to borrow is not in the catalogue")
            else:
                print("You are trying to borrow an eRsource, you can access that by one of our devices")
        else:
            print("You are already borrowing 5 books, return one of them to be able to borrow a new one")

    def return_book_process(self, book, bool, damage_description):
        """Method that simulate the process of returning a book"""
        if self.check_resource(book) is True:
            book.set_borrower(None)            
            if bool is True:
                book.set_damage(damage_description)
        else:
            print("The resouurce you are trying to return is not in the catalogue")
            
    def send_notification(self, notification):
        """Method that send a message to everybody is currently borrowing a book"""
        #Updating the borrower list
        for book in self.catalogue:
            if isinstance(book, Books):
                if book.get_availability() is False and book.get_borrower() not in self.borrower_list:
                    self.borrower_list.append(book.get_borrower())
        #Set the notification
        for member in self.borrower_list:
            member.set_notification(notification)   
        if len(self.borrower_list) is 0:
            print("Actually there are no lendee to sent a message to")
       
    def print_books_catalogue(self):
        """Method that print details of all the books currently on the list"""
        print("Book currently on the system catalogue:")
        index = 0
        for resource in self.catalogue: 
            if isinstance(resource, Books):
                index += 1
                print(f"{index}.")  
                resource.print_resource_details()
                    
    def print_e_resource_catalogue(self):
        """Method that print details of all the books currently on the list"""
        print("eResources currently on the system catalogue:")
        index = 0
        for resource in self.catalogue:
            if isinstance(resource, E_Resources):
                index += 1
                print(f"{index}.")
                resource.print_resource_details()
                   

    
