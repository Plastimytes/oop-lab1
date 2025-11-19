### MINI PROJECT TEST: COURIER_LITE
##The project is an engine for campus delivery with the followings concepts: Collections, Iterators, Generators, Multiple Inheritance, Exceptions and a simple CLI workflow
##Python 3.13 used

##File for data structures and inheritance components
import logging
from typing import Literal, Tuple
from datetime import datetime

##MIXINS(Mixin is a class that provides extra methods/attributes for other classes without being intended as a standalone base class)   
#Logging mixin to provide methods for logging events for a specific object
class Identifiable:
     #Enforcing consistent method for retrieving a string ID using Mixin
     def get_id(self) -> str:
          raise NotImplementedError("Subclasses must use get_id()")

class Printable:
               




































#Class and methods for logging events
class LogMixn:
     def log_event(self, message, level='INFO'):
          log_data = {
               'Level': level,
               'Source': self.__class__.__name__,
               'id':getattr(self,'courier_id','N/A'),
               'message': message
          }

          print(f"<{level}> {self.__class__.__name__} {log_data.get('id','')}: {message}")

#Entities-Other required classes
##Class for pickup and drop off points
class Location:
     def __init__(self, pickup_name, dropoff_name):
          self.pickup_name = pickup_name
          self.dropoff_name = dropoff_name

     def motion(self):
          print(f"The pick up was from {self.pickup_name}") 
          print(f"The drop off was from {self.dropoff_name}")

##Class for Order Request  
class Order:
     def __init__(self, order_id, status): 
          self.order_id=order_id
          self.status = status#This will feature once more in the output section

     def ordReq(self):
          print(f"The order is {self.order_id}, and it is {self.status}")

#Creating a class for the courier
class Courier:
     def __init__(self, courier_id, max_carry_cap, current_load):
          self.courier_id = courier_id
          self.max_carry_cap = max_carry_cap
          self.current_load = current_load

     def asgn_order(self, order: Order):
          if len(self.current_load) < self.max_carry_cap:
               self.current_load.append(order)
               order.status = "IS_BEING_MOVED" 
               return True
          return False 

##MULTIPLE INHERITANCE
class BikeCourier(Courier, LogMixn):
     def __init__(self, courier_id):
          super().__init__(courier_id, max_carry_cap=1) 
          self.log_event("Bike Courier starts")

     def deliver_next(self):
          if not self.current_load:
               self.log_event("Nothing to move", level='WARNING')
               return None 

          delivered_order = self.current_load.pop(0)
          delivered_order.status = "DELIVERED"
          self.log_event(f"Order {delivered_order.order_id} delivered to {delivered_order.dropoff_name}.", level='INFO')
          print(f"{delivered_order}")

#EXCEPTIONS
#Base Exception for errors
class Courier_Lite_Error(Exception):
     pass  

#When no courier is found
class Courier_Unavailable_Error(Courier_Lite_Error):
     pass  