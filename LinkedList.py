from __future__ import annotations
from typing import Optional, Any,Callable
from Link import Link 

def identity(x:Any)->Any: 
   '''default function to get the key for each element of the list'''
   return x 

class LinkedList(object): 
   '''Linkedlist Class'''     
   def __init__(self:LinkedList)->None: 
      '''Initializes a linkedlist
      args:
         self
      returns:
         None'''       
      self.__first = None      
 
   def getFirst(self:LinkedList)->Optional[Link|None]: 
      '''reader for first link
      args:
         self
      returns:
         None or Link obj'''
      return self.__first 
   
   def setFirst(self:LinkedList, link:Link|None)->None: 
      '''setter of link
      args:
         self
         link object
      returns:
         None'''  
      if link is None or isinstance(link, Link): 
         self.__first = link   
      else:
         raise Exception("First link must be Link or None")
 
   def getNext(self:LinkedList)->Link|None:
      '''First link is next
      args:
         self
      returns:
         None or link''' 
      return self.getFirst()    
   
   def setNext(self:LinkedList, link:Link|None)->None: 
      '''setting First link is same as next
      args:
         self
         link object
      returns:
         None'''
      self.setFirst(link)
 
   def isEmpty(self:LinkedList)->bool:
      '''Test for empty list
      args:
         self
      returns:
         bool'''
      return self.getFirst() is None  
 
   def first(self:LinkedList)->Any:
      '''Return the first item(data) in the list
      args:
         self
      returns:
         any type of data'''
      if self.isEmpty():       
         raise Exception('No first item in empty list')
      if self.getFirst() is not None:
         return self.getFirst().getData()  # type: ignore
      
   def traverse(self:LinkedList,func:Callable[[Any], None]=print)->None:
      '''applying a functions to each item in the list
      args:
         self
         func that has to be applied
      returns:
         None'''
      link = self.getFirst()    
      while link is not None:   
         func(link.getData())   
         link = link.getNext()  
 
   def __len__(self:LinkedList)->int:
      '''Gets length of list
      args:
         self
      returns:
         int that reprsents length'''
      l = 0
      link = self.getFirst()    
      while link is not None:   
         l += 1                 
         link = link.getNext() 
      return l
 
   def __str__(self:LinkedList)->str: 
      '''String reprsentation of linkedlist
      args:
         self
      returns:
         str'''          
      result = "["              
      link = self.getFirst()    
      while link is not None:   
         if len(result) > 1:   
            result += " > "    
         result += str(link)    
         link = link.getNext()  
      return result + "]"    
      
   def insert(self:LinkedList, data:Any)->None:  
      '''To insert new data at start of list
      args:
         self
         data
      returns:
         None'''      
      link = Link(data,self.getFirst()) 
      self.setFirst(link)          
 
   def find(self:LinkedList, goal:Any, key:Callable[[Any], Any]=identity)->None|Link: 
      '''Find the 1st Link whose key matches
      args:
         self
         goal target 
         key default equal to identity
      returns:
         None or link'''
      link = self.getFirst()       
      while link is not None:     
         if key(link.getData()) == goal:  
            return link        
         link = link.getNext()    
 
   def search(self:LinkedList, goal:Any, key:Callable[[Any], Any]=identity)->Any|None:
      '''find 1st item whose key matches goal
      args:
         self
         goal target 
         key default equal to identity
      returns:
         None or dat'''
      link = self.find(goal, key)  
      if link is not None:        
         return link.getData()
 
   def insertAfter(self:LinkedList, goal:Any, newDatum:Any,key:Callable[[Any], Any]=identity)->bool:
      '''To insert new data after the first link
      args:
         self
         goal target 
         new data
         key default equal to identity
      returns:
         bool'''
      link = self.find(goal, key)  
      if link is None:            
         return False              
      newLink = Link(              
         newDatum, link.getNext()) 
      link.setNext(newLink)        
      return True
   
   def deleteFirst(self:LinkedList)->Any:
      '''to Delete first Link
      args:
         self
      returns:
         any'''
      if self.isEmpty():            
         raise Exception("Cannot delete first of empty list")
      first = self.getFirst() 
      if first is not None:      
         self.setFirst(first.getNext()) 
         return first.getData()         
 
   def delete(self:LinkedList, goal:Any,key:Callable[[Any], Any]=identity)->None|Any:
      '''To delete key which is same as goal
      args:
         self
         goal target 
         key default equal to identity
      returns:
         None or any'''
      if self.isEmpty(): 
         raise Exception("Cannot delete from empty linked list")
      previous = self               
      while previous.getNext() is not None:
         link = previous.getNext() 
         if link is not None: 
            if goal == key(link.getData()): 
               previous.setNext(       
                  link.getNext())       
               return link.getData()    
         previous = link             
      raise Exception("No item with matching key found in list")
   
   def __iter__(self:'LinkedList')->'__LinkedListIterator':
        '''Call for iterator through linkedlist'''
        return LinkedList.__LinkedListIterator(self.__first)
   
   class __LinkedListIterator:
        '''For an iterator over linkedlist'''
        def __init__(self:'__LinkedListIterator', start:'Link|None')->None:# type: ignore
            '''Initialization of an iterator'''
            self.__current = start

        def __iter__(self: '__LinkedListIterator')->'__LinkedListIterator':# type: ignore
            '''return the iterator'''
            return self

        def __next__(self: '__LinkedListIterator')->Any: # type: ignore
            '''To return next elent in the linkedlist'''
            if self.__current is None:
                raise StopIteration
            data = self.__current.getData()
            self.__current = self.__current.getNext()
            return data