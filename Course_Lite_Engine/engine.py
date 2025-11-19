from .models import * #Importing from the models.py file

##COLLECTIONS AND DATA STRUCTURES
#Creation of main class to manage the other objects
class Courier_Lite_Engine:
    def __init__(self):
        self.couriers = {}# Dictionary used here because changes are not required
        self.locations = {}
        self.pending_orders = []#This can change since these orders are yet to be picked up 
        self.moving_orders = {}
    def load_data(self, hubs_path, riders_path, parcels_path):
        #Initialize the engine from the CSV data files
        print(f"Engine: Loading data from  {hubs_path}, {parcels_path}, {riders_path}")

##ITERATORS AND GENERATORS  
#Generator to yeild couriers carrying orders
    def get_cours_by_load(self):
         for courier in self.couriers.values():
              if courier.current_load:
                   yield courier

#Iterator
    def __iter__(self):
         return iter(self.pending_orders)
    
def try_assign_order(self):
     pass

def process_delivery(self, courier_id):
     if courier_id in self.couriers:
          courier = self.couriers[courier_id]
          courier.deliver_next()
     else:
          raise ValueError(f"Courier {courier_id} not found")
     
           
