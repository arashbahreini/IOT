from health import execute_healt
from moisture import main
import threading

print("Wich applications do you prefer to run ?")
# run_health = input("Health ? (Y/N)")
run_moisture = input("Moisture ? (Y/N)")

health_thread = {}
moisture_thread = {}
# if (run_health == 'y'):
#     health_thread = threading.Thread(target=execute_healt, args=())
#     health_thread.start()

if (run_moisture == 'y'):
    moisture_thread = threading.Thread(target=main,args=())
    moisture_thread.start()
