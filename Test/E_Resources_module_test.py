# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:52:52 2018

@author: SDis
"""

import unittest
from Code.E_Resources_module import E_Resources
from Code.Devices_module import Devices



class Test_E_Resources(unittest.TestCase):
    """Test Class for E_Resources Class"""
    
    def test_eResource_creation(self):
        """Test for eResource creation"""
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        self.assertEqual(e1.get_title(), "1984")
        
    def test_set_title(self):
        """Test for set_get_title methods"""
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        e1.set_title("Animal Farm")
        self.assertEqual(e1.get_title(), "Animal Farm")

    def test_set_author(self):
        """Test for set_get_author methods"""
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        e1.set_author("Samuel Beckett")
        self.assertEqual(e1.get_author(), "Samuel Beckett")        

    def test_set_publisher(self):
        """Test for set_get_publisher methods"""
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        e1.set_publisher("Bloomsbury")
        self.assertEqual(e1.get_publisher(), "Bloomsbury")    
 
    def test_set_yer(self):
        """Test for set_get_year methods"""
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        e1.set_year("1950")
        self.assertEqual(e1.get_year(), "1950")  
        
    def test_add_device(self):
        """Test for add_device method"""
        e1 = E_Resources("1984", "George Orwell", "Harvill Secker", "1949")
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        self.assertEqual(len(e1.device_list), 0) 
        e1.add_device(d1)
        self.assertIn(d1, e1.device_list) 

        
if __name__ == '__main__':
    unittest.main()
    
    