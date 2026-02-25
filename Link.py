from __future__ import annotations

class Link(object):       
   def __init__(self:Link, data:object, next:Link|None=None)->None: 
      '''Initialize a Link object
      args:
         data any obj that is stored in link
         next: refrence to next link'''
      self.__data = data      
      self.__next = next     
 
   def getData(self:Link)->object:
      '''Return the data stored in this link
      returns:
         a object tthat reprsents data'''
      return self.__data
 
   def setData(self:Link, data:object)->None:
      '''Change the datum in this Link
      args:
         data any object
      returns:
         None'''
      self.__data = data
 
   def getNext(self:Link)->Link|None: 
      '''Return the next link
      returns:
         next link or none'''
      return self.__next 
 
   def setNext(self:Link, link:Link|None)->None: 
      ''' Change the next link to a new Link
      args:
         link the next lin k that needs to be set
      returns:
         None''' 
      if link is None or isinstance(link, Link): 
         self.__next = link
      else:
         raise Exception("Next link must be Link or None")
 
   def isLast(self:Link)->bool:
      '''Test if link is last in the chain
      returns;
         a bool value that hows if the link is last'''
      return self.getNext() is None  
 
   def __str__(self:Link)->str:
      '''Make a string representation of link
      returns:
         a str that represents a link'''
      return str(self.getData())
