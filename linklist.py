# -*- coding: utf-8 -*-
"""
Created on Thu May 11 22:11:04 2017

@author: njcx
"""

class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinklList(object):
    def __init__(self,head = None):
        self.head = head
    def append(self,new_node):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            
        
            