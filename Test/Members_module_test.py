# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 18:08:05 2018

@author: SDis
"""

import unittest
from Code.Members_module import Members
from Code.Books_module import Books



class Test_Members(unittest.TestCase):
    """Test Class for Members Class"""
    
    def test_member_creation(self):
        """Test for member creation"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        self.assertEqual(m1.get_surname(), "Blackmore")
        
    def test_set_name(self):
        """Test for set_get_name methods"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        m1.set_name("Ritchie")
        self.assertEqual(m1.get_name(), "Ritchie")
        
    def test_set_surname(self):
        """Test for set_get_surname methods"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        m1.set_surname("Page")
        self.assertEqual(m1.get_surname(), "Page")
        
    def test_set_date_of_birth(self):
        """Test for set_get_date_of_birth methods"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        m1.set_date_of_birth("9-01-1944")
        self.assertEqual(m1.get_date_of_birth(), "9-01-1944")
        
    def test_set_residence(self):
        """Test for set_get_residence methods"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        m1.set_residence("London")
        self.assertEqual(m1.get_residence(), "London")
        
    def test_get_borrowed_books_lengh_add_book(self):
        """Test for get_borrowed_books_lengh and add_book methods"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(m1.get_borrowed_books_lengh(), 0)
        m1.add_book(b1)
        self.assertEqual(m1.get_borrowed_books_lengh(), 1)

    def test_get_borrowed_books(self):
        """Test for get_books_borrowed method"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        m1.add_book(b1)
        self.assertIn(b1, m1.get_borrowed_books())
        
    def test_set_notifications(self):
        """Test for set_get_notifications method"""
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        m1.set_notification("Please return book")
        self.assertEqual(m1.get_notifications(), "-Please return book- ")
        m1.set_notification("Please return book")
        self.assertEqual(m1.get_notifications(), "-Please return book- -Please return book- ")
        
        
if __name__ == '__main__':
    unittest.main()
    
