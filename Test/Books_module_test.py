# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 00:22:34 2018

@author: SDis
"""

import unittest
from Code.Books_module import Books



class TestBooks(unittest.TestCase):
    """Test Class for Books Class"""
    
    def test_book_creation(self):
        """Test for book creation"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(b1.get_title(), "1984")
        
    def test_set_title(self):
        """Test for set_get_title methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_title("Animal Farm")
        self.assertEqual(b1.get_title(), "Animal Farm")

    def test_set_author(self):
        """Test for set_get_author methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_author("Samuel Beckett")
        self.assertEqual(b1.get_author(), "Samuel Beckett")        

    def test_set_publisher(self):
        """Test for set_get_publisher methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_publisher("Bloomsbury")
        self.assertEqual(b1.get_publisher(), "Bloomsbury")    
 
    def test_set_year(self):
        """Test for set_get_year methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_year("1950")
        self.assertEqual(b1.get_year(), "1950")    
        
    def test_set_ISBN(self):
        """Test for set_get_ISBN methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_ISBN("0123456789123")
        self.assertEqual(b1.get_ISBN(), "0123456789123") 
        
    def test_set_wrong_ISBN(self):
        """Test for set_get_ISBN methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_ISBN("a12345678912")
        self.assertEqual(len(b1.get_ISBN()), 13) 
        self.assertNotEqual(b1.get_ISBN(), "112345678912")   
    
    def test_set_damages(self):
        """Test for set_get_damages methods"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        b1.set_damages("cut at page 15")
        self.assertEqual(b1.get_damages(),"-cut at page 15- ") 
        b1.set_damages("stain at page 137")
        self.assertEqual(b1.get_damages(), "-cut at page 15- -stain at page 137- ")  
        
    def test_get_availability(self):
        """Test for get_availability method"""
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(b1.get_availability(), True) 
        b1.borrower = "Jack"
        self.assertEqual(b1.get_availability(), False)  
        
        
if __name__ == '__main__':
    unittest.main()
    
    
    
    
    