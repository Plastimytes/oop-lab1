import sys
from .engine import CourierLiteEngine
from .models import CourierLiteError, Location, Order, FootCourier

def setup_initial_data(engine: CourierLiteEngine):
    """Placeholder for initial setup when not using CSVs."""
    loc_A = Location("Main Gate")
    loc_B = Location("Library")
    engine.add_location(loc_A)
    engine.add_location(loc_B)
    
    courier_1 = FootCourier(101)
    engine.add_courier(courier_1)
    
    # Add a sample pending order
    engine.add_order(Order(1001, loc_A, loc_B))

def run_cli():
    """Main CLI execution loop."""
    engine = CourierLiteEngine()
    
    # 1. Load Data (or setup initial state)
    try:
        engine.load_data("data/hubs.csv", "data/riders.csv", "data/parcels.csv")
    except FileNotFoundError:
        print("Warning: CSV data files not found. Setting up basic demo data.")
        setup_initial_data(engine)
        
    print("\n--- CourierLite CLI Ready ---")

    while True:
        try:
            command = input("CLI> ").strip().lower()

            if command in ('exit', 'quit'):
                print("Exiting CourierLite.")
                break
            
            elif command == 'assign':
                engine.try_assign_order()

            elif command.startswith('deliver'):
                _, courier_id_str = command.split()
                courier_id = int(courier_id_str)
                engine.process_delivery(courier_id)

            elif command == 'status':
                print(f"Pending Orders: {len(list(engine))}")
                for courier in engine.get_loaded_couriers():
                    print(f"Courier {courier.courier_id} has {len(courier.current_load)} order(s).")
            
            else:
                print("Unknown command. Try: assign, deliver <id>, status, exit")

        except CourierLiteError as e:
            print(f"ERROR: System logic failed: {e}")
        except Exception as e:
            print(f"UNEXPECTED ERROR: {e}")
            
if __name__ == "__main__":
    run_cli()