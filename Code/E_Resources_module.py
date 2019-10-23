# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:39:41 2018

@author: SDis
"""
from Code.Resources_parent_module import Resources

class E_Resources(Resources):
    """Son class of Resources, inherit main data fields, setters and getters from that. Plus, other methods.""" 
    def __init__(self, title, author, publisher, year):
        super().__init__(title, author, publisher, year)
        self.device_list = []

    def print_resource_details(self):
        """Method that prints all the details of an eResource object"""
        print(f"E-resource Details:\n{super().get_resource_details()}")
    
    def add_device(self, device):
        """Method that add a device to the device list of an eResource object"""
        self.device_list.append(device)
        
        
