from health import execute_healt
from moisture import main
import threading
from db import Context

print("Wich applications do you prefer to run ?")
run_health = raw_input("Health ? (Y/N)")
run_moisture = raw_input("Moisture ? (Y/N)")

health_thread = {}
moisture_thread = {}
context = Context()
if (run_moisture == 'y'):
    moisture_thread = threading.Thread(target=main,args=(context,))
    moisture_thread.start()


if (run_health == 'y'):
     health_thread = threading.Thread(target=execute_healt, args=(context,))
     health_thread.start()

