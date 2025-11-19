import os
import sys
import logging.config
from .engine import Courier_Lite_Engine
from .models import Courier_Lite_Error, Location, Order, BikeCourier

def set_init_data(engine: Courier_Lite_Engine):
    loc_A = Location("Upper Gate")
    loc_B = Location("Dining Hall")
    engine.add_location(loc_A)
    engine.add_location(loc_B)

    courier_1 = BikeCourier(203)
    engine.add_courier(courier_1)

    #Sample pending order
    engine.add_order(Order(3002,loc_A, loc_B))

def load_logging_config(config_path='logging.conf'):
    if os.path.exists(config_path):
        try:
            logging.config.fileConfig(config_path)
            print(f"Logging cofigured using {config_path}")
        except Exception as e:
            print(f"Error loadding logging configuration {e}") 
            logging.basicConfig(level=logging.INFO)
        else:
            print(f"Warning!! Logging configuration file '{config_path}' not found") 
            logging.basicConfig(level=logging.INFO)      

def run_cli():
    load_logging_config()
    engine = Courier_Lite_Engine()
    
    try:
        engine.load_data("data/hubs.csv", "data/riders.csv", "data/parcels.csv")
    except FileNotFoundError:
        print("Warning!! Data files not found!") 
        set_init_data(engine)

    print("\n --Courier lite Ready--")

    while True:
        try:
            command = input("CLI >").strip().lower()

            if command in ('exit','quit'):
                print("Leaving Courier_Lite")
                break
            elif command == 'assign':
                engine.try_assign_order()
            elif command.startswith('deliver'):
                _, courier_id_str = command.split()
                courier_id = int(courier_id_str)
                engine.process_delivery(courier_id)
            elif command == 'status':
                print(f"Pending:{len(list(engine))}")
                for courier in engine.get_loaded_couriers():
                    print(f"Courier {courier.courier_id} has {len(courier.current_load)} orders.")
            else:
                print(f"Unknown command")
        except Courier_Lite_Error as e:
            print(f"ERROR! System failure: {e}")
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")

if __name__=="__main__":
    run_cli()
                               