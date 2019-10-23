# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:30:52 2018

@author: SDis
"""

import unittest
from Code.Devices_module import Devices



class Test_Devices(unittest.TestCase):
    """Test Class for Devices Class"""
    
    def test_device_creation(self):
        """Test for device creation"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        self.assertEqual(d1.get_device_type(), "PC")
        
    def test_set_type_device(self):
        """Test for set_get_type_device methods"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        self.assertEqual(d1.get_device_type(), "PC")
   
    def test_set_brand(self):
        """Test for set_get_type_brand methods"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        d1.set_brand("Apple")
        self.assertEqual(d1.get_brand(), "Apple")
        
    def test_set_model(self):
        """Test for set_get_model methods"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        d1.set_model("MacBook Pro")
        self.assertEqual(d1.get_model(), "MacBook Pro")
        
    def test_set_year(self):
        """Test for set_get_year methods"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        d1.set_year("2019")
        self.assertEqual(d1.get_year(), "2019")
        
    def test_set_location(self):
        """Test for set_get_locataion methods"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        d1.set_location("4th Floor")
        self.assertEqual(d1.get_location(), "4th Floor")
        
    def test_set_availability(self):
        """Test for set_availbility method"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        self.assertEqual(d1.check_availability(), True)
        d1.set_availability(False)
        self.assertEqual(d1.check_availability(), False)
        
    def test_get_availability(self):
        """Test for get_availability method"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        self.assertEqual(d1.get_availability(), "Available")
        d1.set_availability(False)
        self.assertEqual(d1.get_availability(), "Unavailable")
    
    def test_set_repair_upgrade(self):
        """Test for set_repair_upgrade method"""
        d1 = Devices("PC", "Dell", "xps", "2018","3rd Floor")
        d1.set_repair_upgrade("New RAM 16Gb")
        self.assertEqual(d1.get_repairs_upgrades(), "-New RAM 16Gb- ")        
        d1.set_repair_upgrade("New SSD 256Gb")
        self.assertEqual(d1.get_repairs_upgrades(), "-New RAM 16Gb- -New SSD 256Gb- ")  
   
     
if __name__ == '__main__':
    unittest.main()        
    

        
        
        