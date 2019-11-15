from health import execute_healt

print("Wich applications do you prefer to run ?")
run_health = input("Health ? (Y/N)")
# run_moisture = input("Health ? (Y/N)")

if (run_health == 'y'):
    execute_healt()
