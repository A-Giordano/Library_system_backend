# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:46:11 2018

@author: SDis
"""

import unittest
from Code.System_module import System
from Code.Books_module import Books
from Code.E_Resources_module import E_Resources
from Code.Members_module import Members



class Test_System(unittest.TestCase):
    """Test Class for System Class"""
    
    def test_System_creation(self):
        """Test for Library System creation"""
        s1 = System()
        self.assertEqual(s1.get_library_name(), "default")
        
    def test_set_library_name(self):
        """Test for set_get_library_name methods"""
        s1 = System()
        s1.set_library_name("Andreson")
        self.assertEqual(s1.get_library_name(), "Andreson")

    def test_set_address(self):
        """Test for set_get_address methods"""
        s1 = System()
        s1.set_address("101 St James Rd")
        self.assertEqual(s1.get_address(), "101 St James Rd")
        
    def test_get_catalogue(self):
        """Test for get_catalogue method"""
        s1 = System()
        self.assertEqual(len(s1.get_catalogue()), 0)
           
    def test_add_resource(self):
        """Test for add_resource method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertNotIn(b1, s1.catalogue)
        s1.add_resource(b1)
        self.assertIn(b1, s1.catalogue)
        s1.add_resource(b1)
        self.assertEqual(len(s1.catalogue), 1)
        
    def test_get_catalogue_lengh(self):
        """Test for get_catalogue_lengh method"""
        s1 = System()
        self.assertEqual(s1.get_catalogue_lengh(), 0)
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.add_resource(b1)
        self.assertEqual(s1.get_catalogue_lengh(), 1)
    
    def test_check_resource(self):
        """Test for check_resource method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(s1.check_resource(b1), False)
        s1.add_resource(b1)
        self.assertEqual(s1.check_resource(b1), True)
        
    def test_edit_resource(self):
        """Test for edit_resource method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.edit_resource(b1, "Animal Farm")
        self.assertEqual(b1.get_title(), "1984")
        s1.add_resource(b1)
        s1.edit_resource(b1, "Animal Farm")
        self.assertEqual(b1.get_title(), "Animal Farm")
        
    def test_search_resource(self):
        """Test for search_resource method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(s1.search_resource(b1), None)
        s1.add_resource(b1)
        self.assertEqual(s1.search_resource(b1), b1)
            
    def test_search_by_ISBN(self):
        """Test for search_by_ISBN method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(s1.search_by_ISBN("0123456789123"), 0)
        s1.add_resource(b1)
        self.assertEqual(s1.search_by_ISBN("0123456789123"), 1)
        
    def test_search_by_author(self):
        """Test for search_by_author method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(s1.search_by_author("George Orwell"), 0)
        s1.add_resource(b1)
        self.assertEqual(s1.search_by_author("George Orwell"), 1)
        
    def test_remove_resource(self):
        """Test for remove_resource method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(s1.remove_resource(b1), print())
        s1.add_resource(b1)
        self.assertIn(b1, s1.catalogue)
        s1.remove_resource(b1)
        self.assertNotIn(b1, s1.catalogue)
        
    def test_delete_resource_from_index_position(self):
        """Test for delete_resource_from_index_position method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        self.assertEqual(s1.delete_resource_from_index_position(0), print())
        self.assertEqual(s1.delete_resource_from_index_position(-1), print())
        self.assertEqual(s1.delete_resource_from_index_position(1), print())
        s1.add_resource(b1)
        s1.delete_resource_from_index_position(0)
        self.assertNotIn(b1, s1.catalogue)
        
    def test_lending_process(self):
        """Test for lending_process method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        m2 = Members("Eric", "Eric Clapton", "30-03-1945", "Riplay")
        #test what happens if book not in the catalogue
        s1.lending_process(b1, m1)
        self.assertEqual(b1.get_borrower(), None)
        self.assertNotIn(b1, m1.get_borrowed_books())
        #test what happens if book in the catalogue
        s1.add_resource(b1)
        s1.lending_process(b1, m1)
        self.assertEqual(b1.get_borrower(), m1)
        self.assertIn(b1, m1.get_borrowed_books())
        #test what happens if book already borrowed
        s1.lending_process(b1, m2)
        self.assertEqual(b1.get_borrower(), m1)
        self.assertIn(b1, m1.get_borrowed_books())
        self.assertNotIn(b1, m2.get_borrowed_books())
        #test what happens if eResource is tried to be borrowed
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        s1.add_resource(e1)
        s1.lending_process(e1, m2)
        self.assertNotIn(e1, m2.get_borrowed_books())
        #test what happens if the same book is added 2 times to the same member
        s1.lending_process(b1, m1)
        self.assertEqual(m1.get_borrowed_books_lengh(), 1)
        #test what happens if is tried to borrow more than 5 books:
        #2
        b2 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.add_resource(b2)
        s1.lending_process(b2, m1)
        self.assertEqual(b2.get_borrower(), m1)
        self.assertEqual(m1.get_borrowed_books_lengh(), 2)
        #3
        b3 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.add_resource(b3)
        s1.lending_process(b3, m1)
        self.assertEqual(b3.get_borrower(), m1)
        self.assertEqual(m1.get_borrowed_books_lengh(), 3)
        #4
        b4 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.add_resource(b4)
        s1.lending_process(b4, m1)
        self.assertEqual(b4.get_borrower(), m1)
        self.assertEqual(m1.get_borrowed_books_lengh(), 4)
        #5
        b5 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.add_resource(b5)
        s1.lending_process(b5, m1)
        self.assertEqual(b5.get_borrower(), m1)
        self.assertEqual(m1.get_borrowed_books_lengh(), 5)
        #6
        b6 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        s1.add_resource(b6)
        s1.lending_process(b6, m1)
        self.assertEqual(b6.get_borrower(), None)
        self.assertEqual(m1.get_borrowed_books_lengh(), 5)
        
    def return_book_process(self):
        """Test for return_book_process method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        s1.add_resource(b1)
        s1.lending_process(b1, m1)
        s1.remove_resource(b1)
        #prove that the return of a book doen't take place if not in the ctalogue, 
        #but also that in the remove_resource method should be added somthing to remeove that book from all borrowers
        #or doesn't allow the operation if not returned
        s1.return_book_process(b1, False, "none")
        self.assertEqual(b1.get_borrower(), m1)
        self.assertIn(b1, m1.get_borrowed_books())
        s1.add_resource(b1)
        self.assertEqual(b1.get_borrower(), None)
        self.assertNotIn(b1, m1.get_borrowed_books())
        
    def send_notification(self):
        """Test for send_notification method"""
        s1 = System()
        b1 = Books("1984", "George Orwell", "Harvill Secker", "1949", "0123456789123")
        m1 = Members("Richard", "Blackmore", "14-04-1945", "Weston")
        s1.send_notification("Please return book")
        self.assertEqual(m1.get_notifications(), None)
        s1.add_resource(b1)
        s1.lending_process(b1, m1)
        s1.send_notification("Please return book")
        self.assertEqual(m1.get_notifications(), "-Please return boo- ")
        
        
if __name__ == '__main__':
    unittest.main()
    
